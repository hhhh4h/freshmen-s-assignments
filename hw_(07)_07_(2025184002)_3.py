words = [
  "fresher",
  "soviet",
  "unaltered",
  "drupe",
  "easily",
  "nadir",
  "unseal",
  "alluvium",
  "lupine",
  "rogation",
  "panicle",
  "packer",
  "unwholesome",
  "appetizing",
  "kudos",
  "indentation",
  "introduction",
  "pomade",
  "pushy",
  "orrery",
  "festoon",
  "comfit",
  "ln",
  "linger",
  "astrophysics",
  "suburban",
  "roughly",
  "dotted",
  "hardware",
  "dickens",
  "diastase",
  "penury",
  "kosher",
  "plenipotentiary",
  "gossip",
  "tubercular",
  "bases",
  "peppery",
  "wrestle",
  "catalog",
  "yeoman",
  "carport",
  "hoarse",
  "portuguese",
  "satisfaction",
  "bail",
  "trod",
  "elizabethan",
  "atone",
  "gpo",
  "vulpine",
  "inexhaustible",
  "crow",
  "working",
  "link",
  "literary",
  "wayfarer",
  "unending",
  "knife",
  "tannery",
  "seise",
  "foil",
  "rapscallion",
  "fennel",
  "odour",
  "lighthouse",
  "stepsister",
  "dear",
  "rummage",
  "disassociate",
  "nucleic",
  "mandatory",
  "inessential",
  "conscious",
  "maty",
  "bat",
  "caledonian",
  "fashionable",
  "set",
  "dingle",
  "woodman",
  "aphasia",
  "venom",
  "walkman",
  "garner",
]

word_count = len(words)

# selection sort animation YouTube link:
# https://www.youtube.com/watch?v=92BfuxHn2XE

for i in range(word_count):# 최소값을 word_count 번 구합니다
    min_at = i # i 번째에 일단 최소값 후보가 있음
    for j in range(i+1,word_count): # i+1 부터 끝까지 돌면서 최소값을 찾는다
        if words[j] < words[min_at]: # 알고 있던 최소값보다 작으면
            min_at = j # 이곳이 최소값이다
    temp = words[i]
    words[i] = words[min_at]
    words[min_at] = temp# 최소값 위치(min_at)에 있는 값과 맨 왼쪽(i)의 값을 바꾼다

print(words)

''' 다음과 같이 출력되어야 합니다.
['alluvium', 'aphasia', (중략) 'yeoman']
'''
