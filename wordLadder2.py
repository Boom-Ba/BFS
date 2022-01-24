from collections import deque, defaultdict

start= "hit"
end ="cog"
dict=set(["hot","dot","dog","lot","log"])

def findLadder(start,end, dict):
  dict.add(start)
  dict.add(end)
  level =defaultdict(int)
  bfs(start,end, level, dict)
  path=[]
  res=[]
  dfs(start,end,level,res,path)
  return res

def bfs(start, end, level,dict):
  level[start]=0
  q=deque([start])
  while q:
    cw =q.popleft()
    words= get_next_words(cw, dict)
    for nw in words:
      if nw not in level:
        level[nw]=level[cw]+1
        q.append(nw)
  
def get_next_words(word, dict):
        words = []
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                next_word = word[:i] + c + word[i + 1:]
                if next_word != word and next_word in dict:
                    words.append(next_word)
        return words
  
def dfs(start,end,level,res,path):
  if start ==end:
    res.append(path.copy())
    return 
  
  for word in get_next_words(start,dict):
    if level[word]!=level[start]+1:
      continue
    path.append(word)
    dfs(word,end,level,res,path)
    path.pop()

ret =findLadder(start,end, dict)
print(ret)
