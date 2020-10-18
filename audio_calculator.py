def audio_calc():
    print("This is an audio calculator script ")
    print("This script lets you find any one of these 3 given the others: runtime, bitrate, file size. ")
    print("Runtime in minutes, bitrate in kilobits per second, and storage/file size in megabytes ")
    print("")
    def choose_which_is_missing():
        missing=0
        while str(missing) not in ('a' 'b' 'c' 'd'):
            missing = input("Which is missing? a. runtime, b. bitrate, c. file size, or d. 'What is this thing again?' : ")
    
        if str(missing)=='a':
            print('')
            print('You have chosen: a. runtime ')
            print('')
            runtime_of_a_given_storage_size_at_a_given_bitrate()
            print('')
        elif str(missing)=='b':
            print('')
            print('You have chosen: b. bitrate ')
            print('')
            what_bitrate_should_be_tried()
            print('')
        elif str(missing)=='c':
        	    print('')
        	    print('You have chosen: c. file size ')
        	    print('')
        	    how_much_storage_given_bitrate_and_runtime()
        	    print('')
        elif str(missing)=='d':
            print('')
            print("You have chosen: d. 'What is this thing again? '")
            print('')
            audio_calc()
        else:
            choose_which_is_missing()
            
    choose_which_is_missing()
    
    
    def how_much_storage_given_bitrate_and_runtime():
        print("Given a bitrate and a runtime, this script gives you an approximate file size. ")
        kbitps=float(input("kbitps: "))
        minutes=float(input("number of minutes: "))
        storage=float((((kbitps*minutes*60)/8)/1000))
        print(str(storage) + " megabytes.")
    
    def what_bitrate_should_be_tried():
        print("The purpose of this script is to determine approximately what bitrate somebody should try to use to fit a certain length of something in a certain amount of storage space ") 
        time_in_minutes=(float(input("how many minutes?: "))) 
        storage_in_megabytes=(float(input("how much storage in megabytes?: "))) 
        bitrate_in_kbitps=(((storage_in_megabytes*1000*8)/60)/time_in_minutes) 
        print("suggested bitrate is "+str(bitrate_in_kbitps)+" kilobits per second. ")

    def runtime_of_a_given_storage_size_at_a_given_bitrate():
        print("you give an amount of storage in megabytes and a bitrate in kilobits per second, and it tells you according to math how long of a runtime can fit in that amount of storage at that bitrate, but that doesn't count overhead. ")
        storage_in_megabytes=(float(input("how much storage in megabytes?: ")))
        bitrate_in_kbitps=(float(input("what bitrate in kilobits per second?: ")))
        minutes_in_storage=float((((storage_in_megabytes*1000*8)/bitrate_in_kbitps)/60))
        print(str(minutes_in_storage)+" minutes can fit in "+str(storage_in_megabytes)+" megabytes at "+str(bitrate_in_kbitps)+" kilobits per second.")
        print("that's "+str(minutes_in_storage/60)+" hours. ")



audio_calc()


