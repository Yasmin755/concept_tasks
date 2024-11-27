book_dictionary={
    "The Old Man and the Sea":4,
    "Animal Farm ":9,
    "13Reasons why":5,
    "Longman" :3,
}
max_key=max(book_dictionary,key=book_dictionary.get)
max_value=book_dictionary[max_key]
min_key=min(book_dictionary,key=book_dictionary.get)
min_value=book_dictionary[min_key]
avr_books=sum(book_dictionary.values())/len(book_dictionary)
sorted_books=sorted_dict = dict(sorted(book_dictionary.items(), key=lambda item: item[1], reverse=True))
uniuqe_title=set(book_dictionary.keys())


print(f"most borrowed book : {max_key} -> {max_value}")
print(f"least borrowed book : {min_key} -> {min_value}")
print(f"Average of days of borrowed books : {avr_books}")
print(f"Sorted books : {sorted_books}")
print(f"unique titles : {','.join(uniuqe_title)}")