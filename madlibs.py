# string concatenation
# suppose we want to create a stirng that says " subscribe to _______"
# youtuber = "Jimmy Gao"

# print("Subscribe to " + youtuber)
# print("Subsrcibe to {}".format(youtuber))
# print(f"Subscribe to {youtuber}")

adj = input("Adjective: ")
verb1 = input("Verb 1: ")
verb2 = input("Verb 2: ")
famous_person = input("Famous Person: ")

madlib = f"Computer programming is so {adj}! It makes me so excited because I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}"

print(madlib)
