def dec_function(func):
    def nowexec():
        print("Executing now..")
        func()
        print("Executed..")
    return nowexec

#@dec_function
def who_is_me():
    print("I'm Chetan")


who_is_me = dec_function(who_is_me)
who_is_me()