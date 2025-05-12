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

counts = dict()

# 여기에 과제 내용을 구현하세요
for i in words:
    firstWord = i[0]
    if firstWord in counts:#파이썬에서 디셔너리는 없는 키값을 입력하면 오류가 생겨 확인하기 위해 사용
        counts[firstWord] += 1
    else:
        counts[firstWord] = 1

for letter in sorted(counts.keys()):
    print(f'{letter}:{counts[letter]}', end=',')
print()

''' 다음과 같이 출력되도록 합니다.
a:5,b:3,c:6,d:7,e:2,f:5, ...(생략)... ,v:2,w:5,y:1,
'''


