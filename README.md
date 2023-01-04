# domains_from_har
Parse har file and get domains from them

```
➜ ./domains_from_har.py -h
usage: domains_from_har.py [-h] [-a] harfile

Parcer for har file. Get domains

positional arguments:
  harfile     HAR file

options:
  -h, --help  show this help message and exit
  -a          Make address list as *.rsc


➜ ./domains_from_har.py web.alfabank.ru.har -a
['alfabank.ru', 'alfabank.servicecdn.ru', 'click.alfabank.ru', 'enricher.mfms.ru', 'github.com', 'metrics.alfabank.ru', 'online.alfabank.ru', 'private.auth.alfabank.ru', 'reactjs.org', 'web.alfabank.ru', 'www.w3.org', 'www.yandex.ru']
File web.alfabank.ru.rsc was created successfully.
```