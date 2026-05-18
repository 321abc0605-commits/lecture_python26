# from hangman import Hangman
import hangman as hm

print()
print('========= Hangman =========')


with open('./word_list.txt', encoding='utf-8') as f:
    word_list = []

    for line in f:
        word = line.strip()

        if word != '':
            word_list.append(word)

# 단어 선택
hangman = hm.Hangman(word_list)

print(f'{hangman.display_word}, ({len(hangman.word)}글자)')

while True:
    # 알파벳 입력
    letter = input('>> 알파벳 입력 : ')

    # 정답 확인 
    result = hangman.check_letter(letter)
    if result == hm.Hangman.RIGHT:
        print(f'정답 : {hangman.display_word}')
    elif result == hm.Hangman.WRONG:
        print(f'오답 : {hangman.num_try}회 시도')

    # 승패 확인
    result = hangman.is_win()
    if result == hm.Hangman.WIN:
        print(f'승리 : {hangman.num_try}회 시도')
        break
    elif result == hm.Hangman.LOOSE:
        print(f'패배 : {hangman.word}')
        break
        


