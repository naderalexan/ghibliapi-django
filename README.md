# SENNDER homework task
![get-all-the-movies](x-all-the-y-meme.jpg)

### Run
- `docker-compose up --build`
- Go to `localhost:8000/movies/` or `localhost/films` 

### Test
`docker-compose run backend sh -c "coverage run --source '.' manage.py test && coverage report"`

### Notes
- Main endpoint is `films/` (named as such to align with naming in external API), however, there is a redirect from `movies/` to `films/` to abide by task description
- API runs on port `80` for simplicity, but is `8000` is also exposed to abide by task description
- When accessing `dict`s if the key is required, then direct access is used, otherwise, `get()`. 
This is done on-purpose since not finding non-required keys is not a breaking error
- Tests access the external API, and thus are slow, the other choice would have been mocking the response
- `Black` is used for auto-formating, and runs through a PyCharm integration, however, PyCharm project settings are 
excluded from repo

### Benchmarking using `ab` output
Command:
`ab -n 500 -c 10 http://localhost/films`

Output
```
This is ApacheBench, Version 2.3 <$Revision: 1843412 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient)
Completed 100 requests
Completed 200 requests
Completed 300 requests
Completed 400 requests
Completed 500 requests
Finished 500 requests


Server Software:        nginx/1.18.0
Server Hostname:        localhost
Server Port:            80

Document Path:          /films
Document Length:        0 bytes

Concurrency Level:      10
Time taken for tests:   1.350 seconds
Complete requests:      500
Failed requests:        0
Non-2xx responses:      500
Total transferred:      111500 bytes
HTML transferred:       0 bytes
Requests per second:    370.25 [#/sec] (mean)
Time per request:       27.009 [ms] (mean)
Time per request:       2.701 [ms] (mean, across all concurrent requests)
Transfer rate:          80.63 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.1      0       1
Processing:     6   27   6.1     26      54
Waiting:        5   26   6.2     26      51
Total:          6   27   6.1     26      54

Percentage of the requests served within a certain time (ms)
  50%     26
  66%     29
  75%     31
  80%     31
  90%     33
  95%     37
  98%     44
  99%     46
 100%     54 (longest request)
```