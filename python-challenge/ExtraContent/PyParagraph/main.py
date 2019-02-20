import os
import re

example = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'example.txt')
paragraph1 = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'paragraph_1.txt')
paragraph2 = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'paragraph_2.txt')
file_list = [example, paragraph1, paragraph2]
results = []
for file in file_list:
    word_count = 0
    sentence_count = 0
    average_letter_count = 0
    average_sentence_length = 0
    with open(file, 'r') as myfile:
        file_name = os.path.splitext(os.path.basename(myfile.name))[0]
        data=myfile.read().replace('\n', ' ')
        sentences = re.split("(?<=[.!?]) +", data)
        sentence_count = len(sentences)

        txt_letter_total = 0
        for sentence in sentences:
            words = sentence.split(' ')
            word_count += len(words)
            sentence_letter_total = 0
            for word in words:
                sentence_letter_total += len(word)
            txt_letter_total += sentence_letter_total

        average_letter_count = txt_letter_total / word_count
        average_sentence_length = word_count / sentence_count

        results.append(f"{file_name} Analysis")
        results.append('----------------------------')
        results.append(f"Approximate Word Count: {word_count}")
        results.append(f"Approximate Sentence Count: {sentence_count}")
        results.append(f"Average Letter Count: {average_letter_count}")
        results.append(f"Average Sentence Length: {average_sentence_length}\n")

result_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'results.txt')
f = open(result_file, 'w+')
for result in results:
    print(result)
    f.write(result + '\n')
f.close()
