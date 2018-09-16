from django.test import TestCase
from .models import Event


DESCRIPTION_1 = '''歲末年初是與家人好友歡聚的時刻，在聖誕節前夕透過來自世界不同角落的歌曲，一同欣賞如畫的冬景並歡慶聖誕的喜悅。本場曲目包括耳熟能詳的聖誕歌曲以及帶有爵士搖擺風格的精彩彌撒作品，透過傳統與現代的交會，千百年來不變的心意也能充滿無窮的新意。

本團本著對合唱音樂的熱愛，對自我精提升的要求，不斷開創並發掘多元化曲目。期盼在本場《冬日光景》音樂會能以精緻的西方合唱作品和台北市松韻合唱團真摯優美的歌聲，與愛樂者共饗音樂心靈盛宴。'''  # noqa: E501

ARTIST_1 = '''指揮／何家瑋
鋼琴／許文菁　陳育志
雙簧管／賴思妤
台北市松韻合唱團'''

MUSIC_1 = '''Bob Chilcott: A Little Jazz Mass
Steve Dobrogosz: Mass
Andy Beck: Something Told the Wild Geese
arr. Neil Harmon: 'Twas in the Moon of Wintertime
arr. Thomas Coker: I Wonder as I Wander'''

DESCRIPTION_2 = '''新加坡的譚秀英（Jennifer Tham）和日本的松下耕（Ko Matsushita）與菲律賓的維拉斯科（Jonathan Velasco）為當今亞洲最重要的三位合唱指揮暨合唱教育專家。在許多重要的國際性合唱大賽中獲獎無數，藝術成就受到國際高度的肯定，亦常受邀擔任世界知名合唱活動的評審。而在斐然的比賽成績之外，他們亦常邀請或委託來自世界各地不同國家、不同文化的作曲家譜寫或編寫合唱作品，並透過其所帶領的優秀合唱團隊介紹這些新作品。不僅豐富了合唱的曲目，同時也激發了更多作曲家譜寫合唱作品。

來自新加坡的著名指揮-譚秀英（Jennifer Tham）女士，是以指揮新加坡青年合唱團 (the Singapore Youth Choir) 為名，在她的指揮下此團在星國內外獲獎無數。由於本身也是一位作曲家，透過自己的作品積極地教育年輕的合唱團員與帶領觀眾接近當代的合唱作品。她經常受邀擔任各大國際合唱比賽的評審、研討會與工作坊的講師，也是眾多國際合唱活動中的藝術委員；目前是新加坡青年音樂家協會 (Young Musicians’ Society) 的藝術總監與新加坡青年合唱團的指揮。

本次計畫便是希望透過台北的松韻合唱團與逢友合唱團，結合近年來非常活躍的台中室內合唱團、逢甲合唱團與中部合唱中心，集結兩地四團的資源與人力，邀請新加坡國家文化藝術獎（Singapore Cultural Medallion）得主的譚秀英（Jennifer Tam）女士來台訪問，透過交流印尼、馬來西亞與新加坡的當代合唱作品與風格獨具的節目安排（全場14首歌曲，均為台灣首演），為台灣觀眾帶來東南亞地區文化與藝術上的刺激與饗宴。 我們也期待透過合唱音樂與世界知名詩人作品的結合，帶來對生命的反思，從美妙的樂音與深沉溫暖的詩歌中獲得心靈的 安慰與平衡，促進社會和諧。也希望透過舉辦合唱教育交流講座，使台灣的合唱音樂教育與世界接軌，讓更多藝術的美好種子在台灣的土地上成長、茁壯！'''  # noqa: E501


class EventViewTests(TestCase):
    def setUp(self):
        from datetime import datetime
        # test object 1
        Event.objects.create(
            name='松韻2017冬季音樂會《冬日光景》',
            description=DESCRIPTION_1,
            date=datetime(2017, 12, 23, hour=19, minute=30),
            address='''東吳大學美育中心松怡廳''',
            artist=ARTIST_1,
            music=MUSIC_1,
            price='''350, 500''',
            organizer='''台北市松韻合唱團''',
            url='https://goo.gl/FsJw81')

        # test object 2
        Event.objects.create(
            name='《絕境重聲》',
            description=DESCRIPTION_2,
            date=datetime(2017, 7, 2, hour=14, minute=30))

    def tearDown(self):
        Event.objects.all().delete()

    def test_event_list_view(self):
        response = self.client.get('/event/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'event.html')

    def test_event_detail_view(self):
        response = self.client.get('/event/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'event_detail.html')

        self.assertContains(
            response, '<h1> 松韻2017冬季音樂會《冬日光景》 </h1>', html=True)
        self.assertContains(
            response,
            '''<article> <p>歲末年初是與家人好友歡聚的時刻，在聖誕節前夕透過來自世界不同角落的歌曲，一同欣賞如畫的冬景並歡慶聖誕的喜悅。本場曲目包括耳熟能詳的聖誕歌曲以及帶有爵士搖擺風格的精彩彌撒作品，透過傳統與現代的交會，千百年來不變的心意也能充滿無窮的新意。</p>

<p>本團本著對合唱音樂的熱愛，對自我精提升的要求，不斷開創並發掘多元化曲目。期盼在本場《冬日光景》音樂會能以精緻的西方合唱作品和台北市松韻合唱團真摯優美的歌聲，與愛樂者共饗音樂心靈盛宴。</p></article>''',  # noqa: E501
            html=True)
        self.assertContains(response, '<h2> 演出日期 </h2>', html=True)
        self.assertContains(
            response, '<h3> Dec. 23, 2017, 7:30 p.m. </h3>', html=True)

        self.assertContains(response, '<h2> 演出地點 </h2>', html=True)
        self.assertContains(
            response, '<h3> <p>東吳大學美育中心松怡廳</p> </h3>', html=True)

        self.assertContains(response, '<h2> 演出者 </h2>', html=True)
        self.assertContains(
            response,
            '<h3> <p>指揮／何家瑋<br>鋼琴／許文菁　陳育志<br>雙簧管／賴思妤<br>台北市松韻合唱團</p> </h3>',
            html=True)

        self.assertContains(response, '<h2> 演出曲目 </h2>', html=True)
        self.assertContains(
            response,
            '''<h3> <p>Bob Chilcott: A Little Jazz Mass<br>Steve Dobrogosz: Mass<br>Andy Beck: Something Told the Wild Geese<br>arr. Neil Harmon: &#39;Twas in the Moon of Wintertime<br>arr. Thomas Coker: I Wonder as I Wander</p> </h3>''',  # noqa: E501
            html=True)

        self.assertContains(response, '<h2> 主辦單位 </h2>', html=True)
        self.assertContains(response, '<h3> <p>台北市松韻合唱團</p> </h3>', html=True)

        self.assertContains(response, '<h2> 票價 </h2>', html=True)
        self.assertContains(response, '<h3> <p>350, 500</p> </h3>', html=True)

        self.assertContains(response, '<h2> 購票網址 </h2>', html=True)
        self.assertContains(
            response,
            '<h3><a href="https://goo.gl/FsJw81"> 兩廳院售票系統 </a></h3>',
            html=True)

    def test_event_detail_view_blank_value(self):
        response = self.client.get('/event/2/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'event_detail.html')

        self.assertContains(response, '<h1> 《絕境重聲》 </h1>', html=True)
        self.assertContains(
            response,
            '''<article> <p>新加坡的譚秀英（Jennifer Tham）和日本的松下耕（Ko Matsushita）與菲律賓的維拉斯科（Jonathan Velasco）為當今亞洲最重要的三位合唱指揮暨合唱教育專家。在許多重要的國際性合唱大賽中獲獎無數，藝術成就受到國際高度的肯定，亦常受邀擔任世界知名合唱活動的評審。而在斐然的比賽成績之外，他們亦常邀請或委託來自世界各地不同國家、不同文化的作曲家譜寫或編寫合唱作品，並透過其所帶領的優秀合唱團隊介紹這些新作品。不僅豐富了合唱的曲目，同時也激發了更多作曲家譜寫合唱作品。</p>

<p>來自新加坡的著名指揮-譚秀英（Jennifer Tham）女士，是以指揮新加坡青年合唱團 (the Singapore Youth Choir) 為名，在她的指揮下此團在星國內外獲獎無數。由於本身也是一位作曲家，透過自己的作品積極地教育年輕的合唱團員與帶領觀眾接近當代的合唱作品。她經常受邀擔任各大國際合唱比賽的評審、研討會與工作坊的講師，也是眾多國際合唱活動中的藝術委員；目前是新加坡青年音樂家協會 (Young Musicians’ Society) 的藝術總監與新加坡青年合唱團的指揮。 </p>

<p>本次計畫便是希望透過台北的松韻合唱團與逢友合唱團，結合近年來非常活躍的台中室內合唱團、逢甲合唱團與中部合唱中心，集結兩地四團的資源與人力，邀請新加坡國家文化藝術獎（Singapore Cultural Medallion）得主的譚秀英（Jennifer Tam）女士來台訪問，透過交流印尼、馬來西亞與新加坡的當代合唱作品與風格獨具的節目安排（全場14首歌曲，均為台灣首演），為台灣觀眾帶來東南亞地區文化與藝術上的刺激與饗宴。 我們也期待透過合唱音樂與世界知名詩人作品的結合，帶來對生命的反思，從美妙的樂音與深沉溫暖的詩歌中獲得心靈的 安慰與平衡，促進社會和諧。也希望透過舉辦合唱教育交流講座，使台灣的合唱音樂教育與世界接軌，讓更多藝術的美好種子在台灣的土地上成長、茁壯！</p></article>''',  # noqa: E501
            html=True)
        self.assertContains(response, '<h2> 演出日期 </h2>', html=True)

        self.assertNotContains(response, '<h2> 演出地點 </h2>', html=True)
        self.assertNotContains(response, '<h2> 演出者 </h2>', html=True)
        self.assertNotContains(response, '<h2> 演出曲目 </h2>', html=True)
        self.assertNotContains(response, '<h2> 主辦單位 </h2>', html=True)
        self.assertNotContains(response, '<h2> 票價 </h2>', html=True)
        self.assertNotContains(response, '<h2> 購票網址 </h2>', html=True)

    def test_event_detail_view_404(self):
        response = self.client.get('/event/3/')
        self.assertEqual(response.status_code, 404)
