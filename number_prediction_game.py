import random
import time

while True:                 
                point_a = int("0");
                point_b = int("0");    
                def generate_first_num():
                    number = random.randint(0,2)
                    global NumberStoreA
                    NumberStoreA =[];
                    NumberStoreA.append(number);
                    ProgramB()

                def ProgramB():
                    global point_b
                    total_attempt = 5;
                    number_of_guesses = 0;
                    while number_of_guesses < total_attempt:
                            number_of_guesses += 1
                            guess_number = random.randint(0,2)

                            if NumberStoreA[-1] < guess_number :
                                print('Your guess is too high')
                                time.sleep(0.5)
                            elif NumberStoreA[-1] > guess_number :
                                print('Your guess is too low')
                                time.sleep(0.5)
                            elif NumberStoreA[-1] == guess_number :
                                print('You guessed the number in ' + str(number_of_guesses) + ' tries!')                      
                                point_b +=1
                                time.sleep(0.5)
                                print('Point_B is:\t'+str(point_b))
                                time.sleep(0.5)
                                generate_again()  
                    if number_of_guesses == total_attempt:
                                print('You did not guess the number for 5 chances')
                                generate_again() 
                def generate_again():
                    number = random.randint(0,2)
                    global NumberStoreB
                    NumberStoreB = [];
                    NumberStoreB.append(number);
                    ProgramA()
                    
                def ProgramA():
                    total_attempt = 5;
                    number_of_guesses = 0;
                    global point_a
                    while  number_of_guesses < total_attempt:
                            number_of_guesses += 1
                            guess_number = random.randint(0,2)
                            if NumberStoreB[-1] < guess_number :
                                print('Your guess is too high')
                                time.sleep(0.5)
                            elif NumberStoreB[-1] > guess_number :
                                print('Your guess is too low')
                                time.sleep(0.5)
                            elif NumberStoreB[-1] == guess_number :
                                print('You guessed the number in ' + str(number_of_guesses) + ' tries!')
                                point_a +=1
                                time.sleep(0.5)
                                print('Point_A is:\t'+str(point_a))
                                time.sleep(0.5)
                                generate_first_num()  
                   
                    if number_of_guesses == total_attempt:
                                print('You did not guess the number for 5 chances')
                                generate_first_num() 
                generate_first_num()
                

    
