def answer(s):

    # filter out dashes becaue we don't need them
    # split string into segments
    minified_string = ""
    for character in s:
        if(character == '>'):
            minified_string += '>'
        if(character == '<'):
            minified_string +="<\n" # add delimiter for later
    minified_string = minified_string.splitlines()
    print(minified_string)

    # count everything
    count = 0
    result = 0
    for segment in minified_string:
        if (segment.count("<")==1):
            segmentCount = segment.count(">")
            count += segmentCount
            segmentResult = count * 2
            result += segmentResult

    return result

test01 = ">----<"
test02 = "<<>><"
test03 = "------------->-><-><-->-"
test04 = ">>"
test05 = "<<"
test06 = ">--------------------------<<"
test07 = "><><"
test08 = "<<<<<<<<<<<"

print(answer(test01))
print(answer(test02))
print(answer(test03))
print(answer(test04))
print(answer(test05))
print(answer(test06))
print(answer(test07))
print(answer(test08))