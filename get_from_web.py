import requests


def get_from_web(download_url, headers=None, num_recurr=1, f2save=None, n_attempts=2):

    if headers is None:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1"
            }
    
    r = requests.get(download_url, headers=headers)        
    if not r.status_code == requests.codes.ok:  # pylint: disable=no-member
        print("FAILED to get url:%s reason:[%s] __%d attempt" %(download_url, r.reason, num_recurr))

        #processing failed files - 2nd attempt
        if num_recurr < n_attempts:
            #inkrementujemy num_recurr
            num_recurr = num_recurr + 1

            #wolamy rekurencyjnie avget_daily dla plikuow, dla ktorych sie nie udalo
            _, r = get_from_web(download_url, headers=headers, num_recurr=num_recurr, f2save=None, n_attempts=n_attempts)

    
    if not r.status_code == requests.codes.ok:  # pylint: disable=no-member            
        #koniec filma
        return -1, r
  

    #save 2 disk
    if f2save is not None:
        with open(f2save, mode='wb') as localfile:
            localfile.write(r.content)

    #status, content
    return 1, r

