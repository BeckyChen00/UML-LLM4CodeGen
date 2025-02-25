# Turgutlu football team has more than one football player. A soccer player can be transferred to the football team. A football player can be sold to another football team. The system can perform the first eleven and spare team listing operations. Football players have team, name, age, and number information. Each football player has a different duty and plays football according to their position. Positions are forward, midfield, and defense. There are strikers in the forward, and they play to score goals. There is a goalkeeper in the defense, and he plays to clear the ball. There are midfielders in the midfield, distributing the ball around the pitch. On the system, when the striker scores goals, the system announces his number and name. When the goalkeeper saves the goal, the system announces his number and name.

# 图古特鲁足球管理系统
# 1）管理运动员：包括球队、姓名、年龄和号码。允许将足球运动员调入或调出足球队。支持将足球运动员卖给其他足球队的操作。
# 2）配置足球队：
# 添加/删除阵容。阵容中的球员一定是球队中的球员。
# 添加/删除球员。删除球员，并且从阵容中删除。（不给 ‘并且从阵容中删除’条件是否给出正确结果 ）
# 首发阵容（前11个球员）和替补队的入队操作。根据球员的位置（前锋、中场、防守）分配职责。
# 多名前锋运动员的目的是进球。一名守门员在防守，踢解围球。中场有中场球员，在球场上分配球。
# 首发球员：分配球员的上场位置。
# 不能既是首发球员又是替补球员。

descriptionList = [
"""A football management system, with the following specific requirements:
1) Manage player information, including name and age.
2) Team have transfer operation. Allows football players to be transferred in or out of the football team. Supports selling football players to other football teams.
3) Configure the starting lineup for each match. The starting lineup must include 11 players. Each start lineup player must be assigned a position, including forward, midfield, defender, and goalkeeper. There must be 1 and only 1 goalkeeper in the starting lineup.
4) Configure the substitute lineup for each match. The substitute lineup includes up to 7 substitute players. A player cannot appear in the starting lineup at the same time.
5) Only players who join the team can be added to the starting lineup and substitute lineup.
6) Remove players from the starting/substitute lineup. Before removing a player from the lineup, validate whether the player is in the lineup.
7) Remove players from the team. When a player is being removed from a team, the player must be removed from the lineup of a match that has not been performed.
8) The team can participate in multiple matches, and the starting lineup and substitute lineup can be different in each match.
"""
,

"""足球管理系统，包含以下需求：
1）管理球员信息，包括所属球队、姓名、年龄和球衣号码。
2）转会操作。允许将足球运动员调入或调出足球队。支持将足球运动员卖给其他足球队的操作。
3）配置比赛事件的首发阵容。首发阵容必须包含11名球员（含1名守门员），至少1名前锋球员，至少2名中场球员，至少3名后卫球员，仅1名守门员。
4）配置替补球员，最多7名替补球员，且不可同时出现在首发阵容中。
5）只有注册球队的球员才能加入比赛阵容。
6）添加/删除球员。新球员必须完成注册才能加入球队。
"""
,
"""A football management system, with the following specific requirements:
1) Manage player information, including team, name, age, and jersey number.
2) Team have transfer operation. Allows football players to be transferred in or out of the football team. Supports selling football players to other football teams.
3) Configure the starting lineup in each match event. The starting lineup must include 11 players, at least 1 forward player (FP), at least 2 midfield players (MP), at least 3 defenders (DF), and only 1 goalkeeper (GK).
4) Configure substitute players in each match event, up to 7 substitute players, and cannot appear in the starting lineup at the same time.
5) Only registered team players can join the match event.
6) Add/remove players. New players must complete league registration and then be added to the team.
"""
,
"""足球管理系统，包含以下需求：
1）管理球员信息，包括所属球队、姓名、年龄、注册状态和球衣号码。
2）球队具有转会操作。允许将足球运动员调入或调出足球队。支持将足球运动员卖给其他足球队的操作。
3）每场比赛需要配置首发阵容。首发阵容必须包含11名球员（含1名守门员），至少1名前锋球员，至少2名中场球员，至少3名后卫球员，仅1名守门员。
4）每场比赛需要配置替补阵容，最多7名替补球员，且不可同时出现在首发阵容中。
5）只有加入球队的球员才能加入首发阵容和替补阵容。
6）球队可以添加/删除球员。添加新球员需要先注册球员信息，再加入球队。删除球员，从球队中删除，且从阵容中删除。
7) 球队可以参与多场比赛，每场比赛的首发阵容和替补阵容可以不同。
"""
,

]


umlList = ["""
```plantuml
@startuml

class FootballPlayer {
  - string name
  - int age
}

class Match {
  - date eventDate
  - Map<FootballPlayer, Position> startingLineup
  - List<FootballPlayer> substituteLineup
  
  + removePlayer(footballPlayer)
  + addPlayerToStartingLineup(footballPlayer, position)
  + addPlayerToSubstituteLineup(footballPlayer)  
}
           
class Team {
  - name: String
  - List<Mach> participatedMatches
  
  + removePlayer(footballPlayer)
  + transferPlayer()
  + sellPlayerTo(Team)
}

enum Position {
  forward
  midfield
  defender
  goalkeeper
}

Match "1" -- "0..*" FootballPlayer : startingLineup
(Match, FootballPlayer) .. Position
           

Match "1" -- "0..*" FootballPlayer : substituteLineup


Team "1" -- "1..*" FootballPlayer : contains >

Team "1" -- "0..*" Match : getparticipatedMatches

@enduml
```"""
]


 


