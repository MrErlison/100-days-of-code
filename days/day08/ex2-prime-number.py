#Write your code below this line ๐
def prime_checker(number):
    for i in range(2, number):
        if number % i == 0:
            print("It's not a prime number.")
            return False

    print("It's a prime number.")
    return True

#Write your code above this line ๐
    
#Do NOT change any of the code below๐
if __name__ == "__main__":
    n = int(input("Check this number: "))
    prime_checker(number=n)
