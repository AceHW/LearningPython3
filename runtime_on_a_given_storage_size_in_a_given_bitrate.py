def runtime_of_a_given_storage_size_at_a_given_bitrate():
    storage_in_megabytes=(float(input("how many megabytes?: ")))
    bitrate_in_kbitps=(float(input("what bitrate in kilobits per second?: ")))
    minutes_in_storage=float((((storage_in_megabytes*1000*8)/bitrate_in_kbitps)/60))
    print(str(minutes_in_storage)+" minutes can fit in "+str(storage_in_megabytes)+" megaytes at "+str(bitrate_in_kbitps)+" kilobits per second.")
    print("that's "+str(minutes_in_storage/60)+" hours. ")

runtime_of_a_given_storage_size_at_a_given_bitrate()