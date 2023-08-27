# write file

# rewrite the file
with open("novel.txt", "w") as f:
    f.write(
        "So what do we have here? You can see that we're using the with block pattern we discussed in the previous video to open a file called novel.txt. You might also guess that using the write method on a file object writes contents to it instead of reading from it. The second argument to the open method is new though. So what does the w mean? File objects can be opened in several different modes. A mode is similar to a file permission. It governs what you can do with the file you've just opened. By default, the open function uses the r mode, which stands for read only. You get an error if you try to write to a file opened in read only mode. Since read only is the default, we don't have to pass the R as a second argument when we just want to read the file. Writing however is a whole different story. The w character tells the open function that we want to open the file for writing only. If the file doesn't exist then Python will create it. If the file does exist, then its current contents will be overwritten by whatever we decide to write using our scripts. It's important to remember that when opening a file in write only mode, you can't read its contents. If you try to, the interpreter raises an error. If you want to add content to a file that already exist, you can do that by using other modes like a for appending content at the end of an existing file. Or r+ for read-write mode, where you can both read contents and overwrite it. This has tripped up a lot of us more than once. So I'll say this again. If you open a file for writing and the file already exists, the old contents will be deleted as soon as the file is opened. Yikes, imagine accidentally deleting important content in a file. So remember, double check that you're opening the right file using the right mode. For example, if you're generating a log file of events that your program came across, you probably want to open the file using append, a mode. Opening it in write, w mode, would mean you'd write over any previous entries in that file, and that's not a good idea for a log file. Or if you're generating a report and wants to write it out to a new file using the write, w mode, you probably want to check if the file exists, to avoid losing any previous contents. We'll learn how to check if a file exists in an upcoming video. And finally, what's that lonely looking 30 doing hanging out at the end of our code? That's return value of the write method. When successful, this method returns the number of characters that it wrote. So in this case, 30. Along with read only, write, append, and read-write, the open function supports a bunch of other modes. You'll find all the documentation on this in the official reference, which we'll link to in the next reading. Okay, and breathe, nice job. You just learned some complex things. It might not make sense right away. So have a look at the cheat sheet coming up, which puts all the information in one place for you. And remember, if you feel stuck at any point, you can always rewatch the videos or ask for help in the discussion forums. Over the last few videos, you learned how to open and read a file. How to iterate through a file and finally how to write a file. We use these operations a lot when working with files. So they're super important to know how to use. So head on over to check out the cheat sheet now, and after that, we get some hands on practice with all this and in Jupyter Notebook."
    )

# append the file
with open("novel.txt", "a") as f:
    f.write(
        "new text"
    )
    
# read and write the file
with open("novel.txt", "r+") as f:
    f.write(
        "new text"
    )