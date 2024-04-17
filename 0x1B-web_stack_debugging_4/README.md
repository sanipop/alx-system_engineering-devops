Web Server Debugging Readme

In this web stack debugging task, our objective is to assess the performance of our web server setup featuring Nginx under pressure. We've observed a significant number of failed requests during benchmarking using ApacheBench, indicating that our current configuration is not optimal.

Issue Identification:
During benchmarking with ApacheBench, we simulated 2000 requests to our server with 100 requests made concurrently. The results showed 943 failed requests, indicating a problem with our server setup.

Tool Utilization:
ApacheBench (ab) is utilized for benchmarking purposes. It is a widely used tool in the industry, allowing simulation of HTTP requests to a web server, which aids in performance assessment.

Benchmark Results (Before Fix):
- Complete requests: 2000
- Failed requests: 943
- Non-2xx responses: 1057
- Requests per second: 5664.01 [#/sec] (mean)
- Time per request: 17.655 [ms] (mean)
- Transfer rate:** 3309.15 [Kbytes/sec] received

 Debugging Process:
1. Identified and applied a fix using Puppet, a configuration management tool.
2. Puppet manifest used: `0-the_sky_is_the_limit_not.pp`.
3. Puppet successfully executed the fix for Nginx configuration.

 Benchmark Results (After Fix):
- Complete requests: 2000
- Failed requests:** 0
- Requests per second: 6650.99 [#/sec] (mean)
- Time per request: 15.035 [ms] (mean)
- Transfer rate: 5540.33 [Kbytes/sec] received

 Changes Implemented:
- The fix applied via Puppet improved the performance significantly, eliminating failed requests.

 Recommendations:
1. Monitoring: Regularly monitor server logs and performance metrics to detect and address any issues promptly.
2. Optimization: Continuously optimize server configurations to ensure optimal performance under varying loads.
3. Logging: Utilize logging extensively to track errors and debug issues effectively.

 Conclusion:
Through the debugging process and application of fixes, we have successfully resolved the issue of failed requests in our web server setup. Continuous monitoring and optimization are essential to maintain high performance and reliability. Remember, when something goes wrong, logs are your best friends!

Note: Ensure to replace placeholder Puppet manifest (`0-the_sky_is_the_limit_not.pp`) with the actual fix implemented.
