

if __name__=='__main__':
    text = "重溫《CHILL CLUB推介》:https://bit.ly/3eoHHiJ"
    start = text.find('http')
    end = min(text[start:].find(" "),text[start:].find("\n"))
    if end == -1:
        end = len(text)
    print(text[start:end])
    print("123")
    print("this is my part")
    print("I love you im Gary")
    print("ily")
    print("hey")
    print("456")