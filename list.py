# list manipulation
import test


# def sum(*numbers):
#     sum = 0
#     for n in numbers:
#         sum += int(n)
#     return sum


def test_sum():
    test.assert_equals(sum(1, 2, 3), 6)
    test.assert_equals(sum(1, 2, 3, 4, 5, 6), 21)
    # assert sum(1,2,3) == 6, 'should be 6'
    # assert sum(1,2,3,4,5,6) == 21, 'should be 21'


def find_it(seq):
    # Cach 1 : vet' can, dem so lan xuat hien cua tung so trong list, neu so lan xuat hien la le return ngay lap tuc
    # neu ko tiep tuc so tiep theo
    # u_seq = set(seq)
    # for n in u_seq:
    # 	n_count = 0
    # 	for i in seq:
    # 		n_count += (0,1)[i==n]
    # 	if n_count % 2 != 0:
    # 		return n
    # Cach 2: su dung ham count cua list
    for n in set(seq):
        if seq.count(n) == 1 or seq.count(n) % 2 != 0:
            return n
    return None


def example_001():
    print('''
	Example 001:
	Given an array of integers, find the one that appears an odd number of times.
	There will always be only one integer that appears an odd number of times.
	// Dich
	Cho 1 day so nguyen, tim so tu nhien co so lan xuat hien la 1 so le.
	Biet rang chi co duy nhat 1 so co so lan xuat hien la 1 so le
	''')
    test.assert_equals(
        find_it([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]), 5)
    test.assert_equals(find_it([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]), -1)
    test.assert_equals(find_it([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5]), 5)
    test.assert_equals(find_it([10]), 10)
    test.assert_equals(find_it([1, 1, 1, 1, 1, 1, 10, 1, 1, 1, 1]), 10)
    test.assert_equals(find_it([5, 4, 3, 2, 1, 5, 4, 3, 2, 10, 10]), 1)


def example_002():
    print('''
		Counting sheep
	''')
    sheeps = [True,  True,  True,  False,
              True,  True,  True,  True,
              True,  False, True,  False,
              True,  False, False, True,
              True,  True,  True,  True,
              False, False, True,  True]

    def count_sheeps(sheeps):
        # 1st-simple way: use count method of list
        # return sheeps.count(True)
        # 2nd: filter and check length
        # sheeps_filter = filter(lambda x: x == True,sheeps)
        # for k in sheeps_filter:
        # 	print(k)
        # return len(list(sheeps_filter))
        # 3rd: python comprehension
        return len([x for x in sheeps if x])

    test.assert_equals(count_sheeps(
        sheeps), 17, "There are 17 sheeps in total, not %s" % count_sheeps(sheeps))


def example_003():
    print("""
	             1
	          3     5
	       7     9    11
	   13    15    17    19
	21    23    25    27    29		

	Calculate the row sums of this triangle from the row index (starting at index 1) e.g.:

	row_sum_odd_numbers(1); # 1
	row_sum_odd_numbers(2); # 3 + 5 = 8	

	""")

    def row_sum_odd_numbers(n):
        if n == 0:
            return 0
        # odd always start from 1 and increment steps equal "2"
        # row 1 : 1 - 1
        # row 2 : 1 , 3 , 5 - 3
        # row 3:  1, 3, 5, 7, 9, 11 - 6
        # row 4:  1, 3, 5, 7, 9, 11, 13, 15, 17, 19 - 10 = 4 * 5/2
        if n == 1:
            return 1
        sum = 0
        max_number = n * (n + 1) - 1
        print(n, max_number)

        while(n > 0):
            sum += max_number
            max_number -= 2
            n -= 1
        return sum

    test.assert_equals(row_sum_odd_numbers(1), 1)
    test.assert_equals(row_sum_odd_numbers(2), 8)
    test.assert_equals(row_sum_odd_numbers(13), 2197)
    test.assert_equals(row_sum_odd_numbers(19), 6859)
    test.assert_equals(row_sum_odd_numbers(41), 68921)


def example_004():	
    """
    Mot so van de khi lam viec voi mang
    1. Mang toan so
    2. Mang toan chuoi
    3. Mang ket hop so va chuoi	
    //
    - Tim kiem
    - Loc
    - Aggregate ( sum )
    """
    from functools import reduce
    a = [1, 2, 3, 4, 1, 1, 2, None, 3, 4, 5, None, 100, 1, 3, 6, 9, 12, 15, 18]
    # tim kiem so lan xuat hien cua so 1 trong mang
    count = 0
    num = 1
    start = 0
    for n in a:
        try:
            # if n == num:
            #     count += 1
            count += 1 if n == num else 0
        except:
            continue
    print("So lan xuat hien cua {} trong mang {} la {}".format(num, a, count))
    # loai bo cac phan tu la None hoac la so le
    a = list(filter(lambda x : x != None and x % 2 != 1, a))
    print("Mang {} sau khi loai bo cac so le va phan tu rong".format(a))
    # sum : tinh trung binh cong cua mang a
    tbc = sum(a) / len(a)
    print("TBC cua mang {} la {}".format(a, tbc))
    # sum: tinh tong cac so chia het cho 3
    cacsochiahetcho3 = []
    tongcacsochiahetcho3 = reduce(lambda prev,current: (cacsochiahetcho3.append(current) or (prev + current) ) if current % 3 == 0 else prev, a, 0)
    print("Tong cac so chia het cho 3 trong mang {} bao gom {} la {}".format(tongcacsochiahetcho3, cacsochiahetcho3, a))

    # songs
    songs = []
    def display_song(idx, song):
    	print('-' * 80)    	
    	print('{}.{} - {} ( views: {}, downloads: {}, pubDate: {} ). Listen at {}'.format(idx, song['name'].title(), song['singer'].capitalize(), song['views'], int(song['downloads']), song['pubDate'], song['youtube_video']))
    	print('-' * 80)
    def new_song(name, singer, pubDate, views, downloads, youtube_video=None):
    	"""
    	song{name,singer,pubDate, views, downloads}
    	"""
    	from datetime import datetime
    	import re
    	return {
    		'name': name,
    		'singer': singer,
    		'pubDate': datetime.strptime(re.sub(",(\s*)", ",", pubDate), "%b %d,%Y"),
    		'views': views,
    		'downloads': downloads,
    		'youtube_video': youtube_video or ''
    	}

    songs.append(new_song(name='Trên tình bạn, dưới tình yêu', singer='Min', pubDate='Nov 14, 2020', views=401239, downloads=133e3, youtube_video='https://www.youtube.com/watch?v=mjv8p4ELa-I&list=RDmjv8p4ELa-I&index=1'))
    songs.extend([
    	new_song(name='Em gì ơi', singer='K-ICM x Jack', pubDate='Oct 5,2019', views=287865512, downloads=1.9e6, youtube_video='https://www.youtube.com/watch?v=cBClD7jylos&list=RDmjv8p4ELa-I&index=2'),
    	new_song(name='XIN CÔ ĐƠN ĐI', singer='K-ICM FT. APJ ', pubDate='Oct 5,2019', views=23396935, downloads=59e3, youtube_video='https://www.youtube.com/watch?v=cBClD7jylos&list=RDmjv8p4ELa-I&index=3'),
    	new_song(name='BẠC PHẬN', singer='K-ICM FT Jack ', pubDate='Apr 16,2019', views=343863907, downloads=1.3e6, youtube_video='https://www.youtube.com/watch?v=cBClD7jylos&list=RDmjv8p4ELa-I&index=4'),
    	new_song(name='SÓNG GIÓ ', singer='K-ICM FT. APJ ', pubDate='Jul 12,2019', views=359865850, downloads=2.1e6, youtube_video='https://www.youtube.com/watch?v=cBClD7jylos&list=RDmjv8p4ELa-I&index=5'),
    	new_song(name='Có Tất Cả Nhưng Thiếu Anh ', singer='Erik', pubDate='Jul 28,2019', views=84593277, downloads=517e3, youtube_video='https://www.youtube.com/watch?v=cBClD7jylos&list=RDmjv8p4ELa-I&index=6'),
    	new_song(name='PHÍA SAU EM ', singer='Kay Trần ft Binz', pubDate='Nov 20,2015', views=72384545, downloads=186e3, youtube_video='https://www.youtube.com/watch?v=cBClD7jylos&list=RDmjv8p4ELa-I&index=7'),    	
    ])
    def display_songs(songs):
	    for i in range(len(songs)):
	    	display_song(idx=i+1, song=songs[i])    	
    # group by singer
    import random
    random.shuffle(songs)
    display_songs(songs)

    def sorted_songs(songs, sort_key='name'):
    	ordered_songs = sorted(songs, key=lambda s : s[sort_key])
    	display_songs(ordered_songs)

    sorted_songs(songs, sort_key='name')
    sorted_songs(songs, sort_key='views')
    sorted_songs(songs, sort_key='downloads')
    sorted_songs(songs, sort_key='pubDate')


def main():
    print('list manipulation')
    example_004()
    # test_sum()
    # example_002()
    # example_003()
    # s = "123456a7"
    # l = list(s)
    # l.pop(-1)
    # l.pop(0)
    # https://www.geeksforgeeks.org/python-program-to-convert-a-list-to-string/
    # s = ''.join(map(str, l))
    # print(''.join(l))


if __name__ == '__main__':
    main()
