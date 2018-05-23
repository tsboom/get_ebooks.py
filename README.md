# get_ebooks.py

A python script to download csv files through FTP, and format data into a bibloader format. 

FTP log-in and domain information needs to be stated `ftp_info.py`. 

This repository includes a non-working example in `ftp_info_example.py`



The data will be changed from CSV format like so:

```
"Document ID","Title","PrintIsbn","EIsbn","Publisher","PublicationCity","PublicationDate","Title Edition","Authors","Lcc","Dewey","Lcsh","Subject","Price Non-Linear USD","Price Unlimited USD","Price 3-User USD","Price 1-User USD","Available for Sale","DDA Available","ATO Available","Full Download Available","STL Available","Fund Code","Full Record URL"
"1656079","Religion and the Racist Right : The Origins of the Christian Identity Movement",="9780807846384",="9781469616148","University of North Carolina Press","Chapel Hill","1997-07-01","2","Barkun, Michael","E184.A1 B245 1997","320.5/6","Anglo-Israelism -- United States -- History.; United States -- Race relations.; White supremacy movements -- United States -- History.","History; Political Science","45.00","67.50","56.25","45.00","Yes","Yes","Yes","Yes","Yes","","https://ebookcentral.proquest.com/lib/usmai/detail.action?docID=1656079"

```

The bibloader format looks like this:

```
9781483156750	bkey=1822018	ACTIVE
9781483153520	bkey=1828979	ACTIVE
9781483163055	bkey=1834312	ACTIVE
```

