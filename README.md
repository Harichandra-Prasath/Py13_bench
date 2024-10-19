This is  Python3.13t, free threaded build's bench. It promises true parrallelism on cpu bound tasks.  
Calculation of Fibonacci number is taken as the target function for the benchmark.  

The Job:  
```python
bench_func() {  
  for n from 30 to 34:  
    fibo(n)  
}
```

Three flows were ran to test the promised.  

1. Sequential Flow
2. Multi-Threaded Flow
3. Multi-Process Flow

Each flow has to execute three jobs.  

**Results**  

| Build | Single Job | Sequential | Multi-Threaded | Multi-Process |  
| --------- | ----------| ---------- | ---------- | ---------- |
| Python3.10 | 2.67373797 | 7.98238497 | 18.14799230 | 2.80847765 |
| Python3.13t | 2.3017162 | 6.81978500 | 2.43141885 | 2.51720853 |  


   
As promised, in Python 3.13, it can leverage multiple cores for cpu bound tasks. Its also said there will be additional 40% overhead for single threaded applications in this new free threaded build compared to older builds. 
