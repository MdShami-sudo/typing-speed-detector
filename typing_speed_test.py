import time

def typing_speed_test():
    test_sentence = "The quick brown fox jumps over the lazy dog"
    
    print("Typing Speed Test")
    print("-----------------")
    print(f"Type the following sentence as fast as you can:\n\n{test_sentence}\n")
    
    input("Press Enter to start...")
    start_time = time.time()  

    user_input = input("\nType here: ")
    
    end_time = time.time()  
    
    elapsed_time = end_time - start_time
    elapsed_time_minutes = elapsed_time / 60  
    
    words_typed = len(user_input.split())
    
    typing_speed_wpm = words_typed / elapsed_time_minutes
    
    print("\nResults:")
    print(f"Time taken: {elapsed_time:.2f} seconds")
    print(f"Words typed: {words_typed}")
    print(f"Typing speed: {typing_speed_wpm:.2f} WPM")

typing_speed_test()
