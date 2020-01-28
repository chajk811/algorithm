def hash_func(genres, plays):
    table = {}
    rank = {}

    for i in range(len(genres)):
        if not table.get(genres[i]):
            table[genres[i]] = {plays[i]: [i]}
            rank[genres[i]] = plays[i]
        else:
            rank[genres[i]] += plays[i]
            if table[genres[i]].get(plays[i]):
                table[genres[i]][plays[i]].append(i)
            else:
                table[genres[i]][plays[i]] = [i]
    return table, rank

def solution(genres, plays):
    hash_table, rank = hash_func(genres, plays)
    rank = sorted(rank.items(), key=lambda x: x[1], reverse=True)
    result = []

    for i in rank:
        genre = i[0]
        songs = sorted(hash_table[genre].items(), key=lambda x: x[0], reverse=True)
        cnt = 0

        for song in songs:
            if cnt == 2:
                break
            if len(song[1]) == 1:
                result.append(song[1][0])
                cnt += 1
            else:
                for j in sorted(song[1])[:2]:
                    if cnt == 2:
                        break
                    result.append(j)
                    cnt += 1

    return result