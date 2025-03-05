import random
import time

def read_questions(filename): #This function reads answer and question datas from the txt file
    with open(filename, "r", encoding="utf-8") as file:
        question_dict = {}
        for i in range(7):#There are 14 questions in total, two questions from each category. Two for loop is used to supply that.
            for k in range(2):
                while True: #random questions selected from each category are added to the dictionary in order
                    answer, question = file.readlines()[random.randint(30*i, (30*i)+29)].strip().split("*")
                    file.seek(0)
                    if answer not in question_dict.keys():
                        question_dict[answer] = question
                        break
    return question_dict

def random_letter(dict):
    total_list = [] #this is a 2D list, it will contain "liste"s.
    harf_index_list = [] #This list will contain the index number of the letters in the answer
    for k, v in dict.items():
        liste = [] #this list will contain the elements that will be returned in order when letters are requested one by one
        bos = "|_| " * len(k) #boxes for empty answer
        for a in range(len(k)):
            harf_index_list.append(a)
        for a in range(len(k)):
            random_index = random.choice(harf_index_list) #random index will be selected
            harf_index_list.remove(random_index) #this random number will be deleted from the list so that it will not be repeated again.
            bos = bos[:(4*random_index+1)]+k[random_index]+bos[(4*random_index+2):] #boxes with letter or letters
            liste.append(bos)
        total_list.append(liste)
    return total_list

def main(dict, list, remaining_time): #the part where the question is given and the answer is submitted, score and time is also calculated in this function
    skor = 0
    ques_num = 0

    for k, v in dict.items():
        ques_num += 1
        i = 0 #how many times letter is asked
        question_start_time = time.time() #time will be start when the question shows up

        print(f"{ques_num}. SORU") #question number
        print()
        print("|_| "*len(k)) #empty boxes for question
        print(f"\n{v} ({len(k)} harfli)\n") #question

        user_option = input("(harf alıyım-->H, cevap ver-->C)\n")#User must enter one of these options

        while user_option.upper() not in ["H", "C"]:
            print("Geçersiz komut girdiniz.")
            user_option = input("(harf alıyım-->H, cevap ver-->C)\n")

        while user_option.upper() == "H":
            print()
            print(list[ques_num-1][i]) #the list created in random_letter() function will be used
            print(f"\n{v} ({len(k)} harfli)\n")
            i += 1 #it will increase with each letter taken
            answer_validity = 1 #this is truth value of the answer. It is nessecary for finish time
            if i == len(list[ques_num - 1]): #if the user asks for all the letters in the word, word will be compilated and no extra score for this question
                skor += (i-1)*100
                break
            skor = skor - 100 #for each letter score will decrease by 100
            user_option = input("(harf alıyım-->H, cevap ver-->C)\n")

            while user_option.upper() not in ["H", "C"]:#inputs except H and C will not be accepte, user will enter the command again
                print("Geçersiz komut girdiniz.")
                user_option = input("(harf alıyım-->H, cevap ver-->C)\n")

        if user_option.upper() == "C":
            user_answer = "".join(input("cevabınızı yazınız: ").split())

            if user_answer.lower() == k.lower():
                skor += int(len(k))*100 #score will be updated
                answer_validity = 1 #the answer is true
                print(f"Tebrikler cevabınız doğru! İşte skorunuz: {skor}")

            else:#This part for wrong answers. I have separated this part according to whether there is a letter intake or not, since i already deacrease the score for each letter.
                if i == 0:
                    skor -= (len(k)*100)
                    answer_validity = 0
                    print(f"Maalesef yanlış cevap verdiniz. Doğru cevap '{k}'. İşte skorunuz: {skor}")
                else:
                    skor = skor + (i * 100) -(len(k)*100)
                    print(f"Maalesef yanlış cevap verdiniz. Doğru cevap '{k}'. İşte skorunuz: {skor}")

        question_end_time = time.time() #Time will not be run out between the questions
        elapsed_question_time = question_end_time - question_start_time
        remaining_time -= elapsed_question_time

        if ques_num < 14:
            print(input("Diğer soruya geçmek için enter'a basınız."))

        if remaining_time >= 0:
            print(f"Kalan süre: {int(remaining_time // 60)} dakika {int(remaining_time % 60)} saniye")

        if remaining_time <= 0:
            # In order not to include the answered question in the score after the time has finished
            if answer_validity == 1:
                skor = skor - int(len(k)) * 100 + (i * 100)
            elif answer_validity == 0:
                skor += (len(k) * 100)

            print("Süre doldu! Oyun sona erdi.")
            print(f"Toplam skorunuz: {skor}")
            break

    return skor, remaining_time

def user_and_skor(username, skor, time): #player information will be added to the dictionary
    user_and_skor_dict = {}
    user_and_skor_dict[username] = [skor, time]
    return user_and_skor_dict

def database(filename, dict):#All players will be stored in this new csv file with their scores and remaining time
    with open(filename, 'a', encoding="utf-8") as file:
        for k, v in dict.items():
            file.write(f"{k},{v[0]},{v[1]}\n")


def top_10(filename):
    with open(filename, 'r', encoding="utf-8") as file:
        data = [line.strip().split(',') for line in file]

    sorted_data = sorted(data, key=lambda row: (int(row[1]), float(row[2])), reverse=True) #All players saved in csv file will be sorted in this part according to their scores then remaining time

    top_10 = sorted_data[:10]
    header = ['Username', 'Score', 'Remaining Time']
    i = 1
    with open('top_users.csv', 'w', encoding="utf-8") as file: #new csv file will be created for top 10 player.
        file.write(','.join(header) + '\n')
        for row in top_10:
            file.write(str(i) + '. ' + ','.join(row) + '\n')
            i += 1

def play_again(filename): #Offers options to play again, exit the game, or view the leaderboard.
    while True:
        options = input("Yeniden denemek için 'Y', oyundan çıkmak için 'Ç', skor tablosunu görmek için 'S' girin: ")
        if options.upper() == 'Y':
            return True

        elif options.upper() == 'Ç':
            return False

        elif options.upper() == 'S':
            print("\nİLK 10 İÇİN SKOR TABLOSU\n")
            with open(filename, "r", encoding="utf-8") as file:
                for line in file:
                    print(line)

        else:
            print("Geçersiz bir seçenek girdiniz. Lütfen 'Y' veya 'Ç' seçeneklerinden birini girin.")


if __name__ == "__main__":
    while True:
        username = input("Lütfen kullanıcı adınızı girin: ")
        print(input("oyuna başlamak için enter'a basın"))
        question_dict = read_questions("soru.txt")
        total_list = random_letter(question_dict)
        start_time = time.time()
        remaining_time = 5 * 60
        skor, remaining_time = main(question_dict, total_list, remaining_time)
        user_and_skor_dict =user_and_skor(username, skor, remaining_time)
        database("database.csv", user_and_skor_dict)
        top_10("database.csv")

        if not play_again("top_users.csv"):
            break