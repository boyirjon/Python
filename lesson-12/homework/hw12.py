# Exercise 1

import threading

# Function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

# Worker function for threads
def check_primes_in_range(start, end, result_list):
    local_primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            local_primes.append(num)
    result_list.extend(local_primes)

# Main function
def threaded_prime_checker(start, end, num_threads=4):
    threads = []
    results = []

    # Divide range into chunks for threads
    step = (end - start + 1) // num_threads
    for i in range(num_threads):
        range_start = start + i * step
        # Last thread takes the remainder
        range_end = start + (i + 1) * step - 1 if i != num_threads - 1 else end
        thread = threading.Thread(target=check_primes_in_range, args=(range_start, range_end, results))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    # Sort results since threads may append in different order
    results.sort()
    return results


# Example usage
if __name__ == "__main__":
    start_range = 1
    end_range = 100
    primes = threaded_prime_checker(start_range, end_range, num_threads=4)
    print(f"Prime numbers between {start_range} and {end_range}:")
    print(primes)

# Exercise 2

import threading
from collections import Counter

# Worker function for each thread
def count_words_in_lines(lines, result_list):
    local_counter = Counter()
    for line in lines:
        words = line.strip().split()
        local_counter.update(words)
    result_list.append(local_counter)  # append thread-local counter


def threaded_word_count(filename, num_threads=4):
    # Read all lines from file
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # Divide lines among threads
    chunk_size = len(lines) // num_threads
    threads = []
    results = []

    for i in range(num_threads):
        start = i * chunk_size
        # Last thread takes remainder
        end = (i + 1) * chunk_size if i != num_threads - 1 else len(lines)
        thread = threading.Thread(target=count_words_in_lines, args=(lines[start:end], results))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for t in threads:
        t.join()

    # Merge results from all threads
    final_counter = Counter()
    for c in results:
        final_counter.update(c)

    return final_counter


# Example usage
if __name__ == "__main__":
    filename = "sample.txt"  # replace with your large file
    word_counts = threaded_word_count(filename, num_threads=4)

    print("Word occurrences in file:")
    for word, count in word_counts.most_common(20):  # show top 20
        print(f"{word}: {count}")
