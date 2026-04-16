import asyncio
import random
import time
from abc import ABC, abstractmethod
from concurrent.futures import ThreadPoolExecutor

# 1. طبقة التجريد (Abstraction Layer) - فرض هيكلية هندسية
class TaskProcessor(ABC):
    @abstractmethod
    async def process(self, data: dict) -> bool:
        pass

# 2. نظام Circuit Breaker - لمنع انهيار النظام عند وجود ثغرات أو ضغط
class CircuitBreaker:
    def __init__(self, failure_threshold=3, recovery_timeout=5):
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout
        self.failures = 0
        self.last_failure_time = 0
        self.state = "CLOSED" # CLOSED, OPEN, HALF_OPEN

    def call(self, func, *args):
        if self.state == "OPEN":
            if time.time() - self.last_failure_time > self.recovery_timeout:
                self.state = "HALF_OPEN"
            else:
                raise Exception("Circuit is OPEN - Request Blocked")

        try:
            result = func(*args)
            self.failures = 0
            self.state = "CLOSED"
            return result
        except Exception as e:
            self.failures += 1
            self.last_failure_time = time.time()
            if self.failures >= self.failure_threshold:
                self.state = "OPEN"
            raise e

# 3. المحرك الرئيسي - يجمع بين Asyncio و ThreadPool للمعالجة الهجينة
class Engine(TaskProcessor):
    def __init__(self):
        self.executor = ThreadPoolExecutor(max_workers=5)
        self.cb = CircuitBreaker()

    def heavy_computation(self, x):
        # محاكاة لعملية تستهلك CPU بكثافة (تفكيك ثغرة أو تشفير)
        if random.random() < 0.2: raise ValueError("Computation Failed")
        return sum(i * i for i in range(x))

    async def process(self, data: dict) -> bool:
        loop = asyncio.get_event_loop()
        try:
            # استخدام Circuit Breaker داخل بيئة Async
            result = await loop.run_in_executor(
                self.executor, 
                self.cb.call, 
                self.heavy_computation, 
                data.get("complexity", 1000)
            )
            print(f"[SUCCESS] Result: {result}")
            return True
        except Exception as e:
            print(f"[ERROR] Logic Failure: {e}")
            return False

# 4. نقطة الانطلاق (Entry Point) - إدارة التدفق (Flow Control)
async def main():
    engine = Engine()
    tasks = [{"complexity": random.randint(1000, 5000)} for _ in range(10)]
    
    # معالجة دفعية (Batch Processing) مع التحكم في الاستهلاك
    results = await asyncio.gather(*[engine.process(t) for t in tasks], return_exceptions=True)
    print(f"\nFinal Engine State: {engine.cb.state}")
    print(f"Success Rate: {results.count(True)}/{len(results)}")

if __name__ == "__main__":
    asyncio.run(main())
            
    
