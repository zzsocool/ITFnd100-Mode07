**Zefeng Shen**  
**August 23, 2020**  
**IT FDN 110A** 
**Assignment07**  
https://github.com/zzsocool/ITFnd100-Mode07


#       Binary File and Error Handling

## Introduction:
```
In this week, I learned about how to create and unpack binary files and how to use expect and extract the error messages and custom the error messages to display to the user. I also learned a little more about how to edit my Github page.
```
## File Mode:
```
This will open a text file called "TestingText" in read-only mode. Take note that only the filename parameter was specified, this is due to the "read" mode being the default mode for the open function.
The access modes available for the open() function are as follows:
•	r: Opens the file in read-only mode. Starts reading from the beginning of the file and is the default mode for the open() function.
•	rb: Opens the file as read-only in binary format and starts reading from the beginning of the file. While binary format can be used for different purposes, it is usually used when dealing with things like images, videos, etc.
•	r+: Opens a file for reading and writing, placing the pointer at the beginning of the file.
•	w: Opens in write-only mode. The pointer is placed at the beginning of the file and this will overwrite any existing file with the same name. It will create a new file if one with the same name doesn't exist.
•	wb: Opens a write-only file in binary mode.
•	w+: Opens a file for writing and reading.
•	wb+: Opens a file for writing and reading in binary mode.
•	a: Opens a file for appending new information to it. The pointer is placed at the end of the file. A new file is created if one with the same name does not exist.
•	ab: Opens a file for appending in binary mode.
•	a+: Opens a file for both appending and reading.
•	ab+: Opens a file for both appending and reading in binary mode.
(Stackabouse, https://stackabuse.com/file-handling-in-python/) (External website)
```
## Binary file:
```
A binary file is a file stored in binary format. A binary file is computer-readable but not human-readable. All executable programs are stored in binary files, as are most numeric data files. In contrast, text files are stored in a form (usually ASCII) that is human-readable.
(Webopedia,https://www.webopedia.com/TERM/B/binary_file.html#:~:text=A%20binary%20file%20is%20a,)%20that%20is%20human%2Dreadable.) (External website)
```
## Pickle:
```
The pickle module implements binary protocols for serializing and de-serializing a Python object structure. “Pickling” is the process whereby a Python object hierarchy is converted into a byte stream, and “unpickling” is the inverse operation, whereby a byte stream (from a binary file or bytes-like object) is converted back into an object hierarchy. Pickling (and unpickling) is alternatively known as “serialization”, “marshalling,” 1 or “flattening”; however, to avoid confusion, the terms used here are “pickling” and “unpickling”.
 The pickle module is not secure. Only unpickle data you trust. It is possible to construct malicious pickle data which will execute arbitrary code during unpickling. Never unpickle data that could have come from an untrusted source, or that could have been tampered with. Consider signing data with hmac if you need to ensure that it has not been tampered with. Safer serialization formats such as json may be more appropriate if you are processing untrusted data

(Docpython,https://docs.python.org/3/library/pickle.html#:~:text=%E2%80%9CPickling%E2%80%9D%20is%20the%20process%20whereby,back%20into%20an%20object%20hierarchy.) (External website)
```
## Try and Except:
```
How try() works?
•	First try clause is executed i.e. the code between try and except clause.
•	If there is no exception, then only try clause will run, except clause is finished.
•	If any exception occured, try clause will be skipped and except clause will run.
•	If any exception occurs, but the except clause within the code doesn’t handle it, it is passed on to the outer try statements. If the exception left unhandled, then the execution stops.
•	A try statement can have more than one except clause
(Geekssforgeeks,https://www.geeksforgeeks.org/python-try-except/) ( External website)

```


Script:

For this week assignment, I started with creating a binary file. Binary file mode was different than normal text file. For writing mode, I input “wb”. For writing a binary file, I used pickle.dump() as shown in figure 1.
```
![Figure 1](https://github.com/zzsocool/ITFnd100-Mode07/blob/master/docs/assignmeng.png "Figure 1")
### Figure 1: Save data to a binary file.

