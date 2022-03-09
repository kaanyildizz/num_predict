import random
import time

while True:
                #Generating PointStore Variables
                PointStoreA = int("0");
                PointStoreB = int("0");    
                def generate_first_num():
                    #Generating first number and adding it to NumberStoreA queue
                    number = random.randint(0,9)
                    global NumberStoreA
                    #Implementing Queue using List 
                    NumberStoreA =[];
                    NumberStoreA.append(number);
                    ProgramB()

                def ProgramB():
                    global PointStoreB
                    #total_attempt was defined this way because it was requested to have 5 attempts in task.
                    total_attempt = 5;
                    number_of_guesses = 0;
                    while number_of_guesses < total_attempt:
                            number_of_guesses += 1
                            guess_number = random.randint(0,9)
                            #Checking if the guess number is equal to the number
                            if NumberStoreA[-1] < guess_number :
                                print('Your guess is too high')
                                time.sleep(0.5)
                            elif NumberStoreA[-1] > guess_number :
                                print('Your guess is too low')
                                time.sleep(0.5)
                            elif NumberStoreA[-1] == guess_number :
                                print('You guessed the number in ' + str(number_of_guesses) + ' tries!')
                                #If prediction is correct then the value of PointStoreB will increase by 1 point
                                PointStoreB +=1
                                time.sleep(0.5)
                                print('Point_B is:\t'+str(PointStoreB))
                                time.sleep(0.5)
                                generate_again()  
                    if number_of_guesses == total_attempt:
                                print('You did not guess the number for 5 chances')
                                generate_again() 
                def generate_again():
                    #If the ProgramB does not know correctly for 5 chances or know correctly the number,
                    #this func. generates a value for programA to know
                    number = random.randint(0,9)
                    global NumberStoreB
                    NumberStoreB = [];
                    NumberStoreB.append(number);
                    ProgramA()
                    
                def ProgramA():
                    total_attempt = 5;
                    number_of_guesses = 0;
                    global PointStoreA
                    while  number_of_guesses < total_attempt:
                            number_of_guesses += 1
                            guess_number = random.randint(0,9)
                            #Checking if the guess number is equal to the number
                            if NumberStoreB[-1] < guess_number :
                                print('Your guess is too high')
                                time.sleep(0.5)
                            elif NumberStoreB[-1] > guess_number :
                                print('Your guess is too low')
                                time.sleep(0.5)
                            elif NumberStoreB[-1] == guess_number :
                                print('You guessed the number in ' + str(number_of_guesses) + ' tries!')
                                #If prediction is correct then the value of PointStoreA will increase by 1 point
                                PointStoreA +=1
                                time.sleep(0.5)
                                print('Point_A is:\t'+str(PointStoreA))
                                time.sleep(0.5)
                                generate_first_num()  
                   
                    if number_of_guesses == total_attempt:
                                print('You did not guess the number for 5 chances')
                                generate_first_num()
                #Running the code at first                
                generate_first_num()
                

    
