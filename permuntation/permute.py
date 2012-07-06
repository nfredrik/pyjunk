def permute(word):
          """
          By Barry Carrol <Barry.Carroll at psc.com>
          on Tutor list, revised (last line) by me.
          """
          retList=[]
          if len(word) == 1:
                  # There is only one possible permutation
                  retList.append(word)
                  print 'Tut'
          else:
                  # Return a list of all permutations using allcharacters
                  for pos in range(len(word)):
                          # Get the permutations of the rest of the word
 
                      permuteList=permute(word[0:pos]+word[pos+1:len(word)])
                          # Now, tack the first char onto each word in the list
                          # and add it to the output
                  for item in permuteList:
                      retList.append(word[pos]+item)
                      
          #return retList
          return list(set(retList)) # make elements of retList unique
 
 
def permuteset(word):
    return list(set(permute(word)))


print permute("121")

print permuteset("121")