from store_patturn import *




class MyApp(QWidget):
    inputallow = False
    printallow = False
    inputvalue = None

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.ttsig = TTsig()

        #1st group
        self.te = QTextBrowser(self)
        self.li = QLineEdit(self)
        self.btn = QPushButton("OK(Enter)", self)
        self.btn.setShortcut("Return")
        self.nextbtn = QPushButton("Next(Up arrow)",self)
        self.nextbtn.setShortcut("Up")

        self.skilscriptte = QTextBrowser(self)
        self.gr6g3roup = QGroupBox('스킬 설명')
        self.gr6g3rid = QGridLayout()
        self.gr6g3rid.addWidget(self.skilscriptte)
        self.gr6g3roup.setLayout(self.gr6g3rid)

        self.groupbox1 = QGroupBox("대화창")
        self.vbox1 = QVBoxLayout()
        self.vbox1.addWidget(self.te)
        self.vbox1.addWidget((self.li))
        self.vbox1.addWidget(self.btn)
        self.vbox1.addWidget(self.nextbtn)
        self.vbox1.addWidget(self.gr6g3roup)
        self.groupbox1.setLayout(self.vbox1)

        ##2nd group-1st part
        self.healthlabel = QLabel("체력",self)
        self.healthlied = QLineEdit(self)
        self.reddicelabel = QLabel("(붉은 주사위",self)
        self.reddicelied = QLineEdit(self)
        self.amountlabel = QLabel("개)",self)

        self.manalabel = QLabel("마력", self)
        self.manalied = QLineEdit(self)
        self.bluedicelabel = QLabel("(푸른 주사위", self)
        self.bluedicelied = QLineEdit(self)
        self.amountlabel2 = QLabel("개)", self)

        self.actlabel = QLabel("행동력", self)
        self.actlied = QLineEdit(self)
        self.maxactlabel = QLabel("개 / ", self)
        self.maxactlied = QLineEdit(self)
        self.amountlabel3 = QLabel("개", self)

        self.maxactlied.setReadOnly(True)
        self.actlied.setReadOnly(True)
        self.bluedicelied.setReadOnly(True)
        self.healthlied.setReadOnly(True)
        self.manalied.setReadOnly(True)
        self.reddicelied.setReadOnly(True)

        self.redrollresultlabel = QLabel("붉은 주사위 굴린 결과:")
        self.bluerollresultlabel = QLabel("푸른 주사위 굴린 결과:")
        self.greenrollresultlabel = QLabel("초록 주사위 굴린 결과:")
        self.redrollresultlied = QLineEdit(self)
        self.bluerollresultlied = QLineEdit(self)
        self.greenrollresultlied = QLineEdit(self)
        self.redrollresultlied.setReadOnly(True)
        self.bluerollresultlied.setReadOnly(True)
        self.greenrollresultlied.setReadOnly(True)

        self.groupbox2 = QGroupBox("자원")
        self.grid2 = QGridLayout()
        self.grid2.addWidget(self.healthlabel,0,0)
        self.grid2.addWidget(self.healthlied,0,1)
        self.grid2.addWidget(self.reddicelabel,0,2)
        self.grid2.addWidget(self.reddicelied,0,3)
        self.grid2.addWidget(self.amountlabel,0,4)
        self.grid2.addWidget(self.manalabel,1,0)
        self.grid2.addWidget(self.manalied,1,1)
        self.grid2.addWidget(self.bluedicelabel,1,2)
        self.grid2.addWidget(self.bluedicelied,1,3)
        self.grid2.addWidget(self.amountlabel2,1,4)
        self.grid2.addWidget(self.actlabel,2,0)
        self.grid2.addWidget(self.actlied,2,1)
        self.grid2.addWidget(self.maxactlabel,2,2)
        self.grid2.addWidget(self.maxactlied,2,3)
        self.grid2.addWidget(self.amountlabel3,2,4)

        self.grid22 = QGridLayout()
        self.grid22.addWidget(self.redrollresultlabel, 0, 0)
        self.grid22.addWidget(self.redrollresultlied, 0, 1)
        self.grid22.addWidget(self.bluerollresultlabel, 1, 0)
        self.grid22.addWidget(self.bluerollresultlied, 1, 1)
        self.grid22.addWidget(self.greenrollresultlabel, 2, 0)
        self.grid22.addWidget(self.greenrollresultlied, 2, 1)

        self.vbox2 = QVBoxLayout()
        self.vbox2.addLayout(self.grid2)
        self.vbox2.addLayout(self.grid22)
        self.groupbox2.setLayout(self.vbox2)

        ##2nd group-1st part
        self.spelluselistte = QTextBrowser(self)
        self.groupbox3 = QGroupBox("<사용할 마법 대기열>")
        self.vbox3 = QVBoxLayout()
        self.vbox3.addWidget(self.spelluselistte)
        self.groupbox3.setLayout(self.vbox3)

        ##2nd group-2st part
        self.allturnbuffte = QTextBrowser(self)
        self.turnbuffte = QTextBrowser(self)
        self.actionbuffte = QTextBrowser(self)
        self.grgroup1 = QGroupBox("<전투 부여 효과>")
        self.grgroup2 = QGroupBox("<턴 부여 효과>")
        self.grgroup3 = QGroupBox("<행동 부여 효과>")
        self.groupbox4 = QGroupBox("<부여 효과>")
        self.grgrid1 = QGridLayout()
        self.grgrid2 = QGridLayout()
        self.grgrid3 = QGridLayout()
        self.vbox4 = QVBoxLayout()
        self.grgrid1.addWidget(self.allturnbuffte,0,0)
        self.grgrid2.addWidget(self.turnbuffte,0,0)
        self.grgrid3.addWidget(self.actionbuffte,0,0)
        self.grgroup1.setLayout(self.grgrid1)
        self.grgroup2.setLayout(self.grgrid2)
        self.grgroup3.setLayout(self.grgrid3)
        self.vbox4.addWidget(self.grgroup1)
        self.vbox4.addWidget(self.grgroup2)
        self.vbox4.addWidget(self.grgroup3)
        self.groupbox4.setLayout(self.vbox4)

        ##2nd group-3st part
        self.attackte = QTextBrowser(self)
        self.defencelied = QLineEdit(self)
        self.defencelied.setReadOnly(True)
        self.faultbtn = QPushButton("[회색이 되면 행동불능!]")

        self.grgroup4 = QGroupBox("방어력")
        self.grgroup5 = QGroupBox("공격대상/공격력")
        self.grgrid4 = QGridLayout()
        self.grgrid5 = QGridLayout()
        self.grgrid4.addWidget(self.defencelied,0,0)
        self.grgrid5.addWidget(self.attackte,0,0)
        self.grgroup4.setLayout(self.grgrid4)
        self.grgroup5.setLayout(self.grgrid5)
        self.vbox5 = QVBoxLayout()
        self.vbox5.addWidget(self.faultbtn)
        self.vbox5.addWidget(self.grgroup4)
        self.hbox5 = QHBoxLayout()
        self.hbox5.addWidget(self.grgroup5)
        self.hbox5.addLayout(self.vbox5)
        self.groupbox5 = QGroupBox("방어력-공격력-행동불능여부")
        self.groupbox5.setLayout(self.hbox5)

        ##2nd group-main
        self.maingroup2 = QGroupBox("당신")
        self.namelied = QLineEdit(self)
        self.namelabel = QLabel("당신의 이름 : ")
        self.hbox = QHBoxLayout()
        self.hbox.addWidget(self.namelabel)
        self.hbox.addWidget((self.namelied))
        self.m2vbox = QVBoxLayout()
        self.m2vbox.addLayout(self.hbox)
        self.m2vbox.addWidget(self.groupbox2)
        self.m2vbox.addWidget(self.groupbox3)
        self.m2vbox.addWidget(self.groupbox4)
        self.m2vbox.addWidget(self.groupbox5)
        self.maingroup2.setLayout(self.m2vbox)





        ##3rd group-1st part
        self.mn1healthlabel = QLabel("체력", self)
        self.mn1healthlied = QLineEdit(self)
        self.mn1reddicelabel = QLabel("(붉은 주사위", self)
        self.mn1reddicelied = QLineEdit(self)
        self.mn1amountlabel = QLabel("개)", self)

        self.mn1manalabel = QLabel("마력", self)
        self.mn1manalied = QLineEdit(self)
        self.mn1bluedicelabel = QLabel("(푸른 주사위", self)
        self.mn1bluedicelied = QLineEdit(self)
        self.mn1amountlabel2 = QLabel("개)", self)

        self.mn1actlabel = QLabel("행동력", self)
        self.mn1actlied = QLineEdit(self)
        self.mn1maxactlabel = QLabel("개 / ", self)
        self.mn1maxactlied = QLineEdit(self)
        self.mn1amountlabel3 = QLabel("개", self)

        self.mn1maxactlied.setReadOnly(True)
        self.mn1actlied.setReadOnly(True)
        self.mn1bluedicelied.setReadOnly(True)
        self.mn1healthlied.setReadOnly(True)
        self.mn1manalied.setReadOnly(True)
        self.mn1reddicelied.setReadOnly(True)

        self.mn1redrollresultlabel = QLabel("붉은 주사위 굴린 결과:")
        self.mn1bluerollresultlabel = QLabel("푸른 주사위 굴린 결과:")
        self.mn1greenrollresultlabel = QLabel("초록 주사위 굴린 결과:")
        self.mn1redrollresultlied = QLineEdit(self)
        self.mn1bluerollresultlied = QLineEdit(self)
        self.mn1greenrollresultlied = QLineEdit(self)
        self.mn1redrollresultlied.setReadOnly(True)
        self.mn1bluerollresultlied.setReadOnly(True)
        self.mn1greenrollresultlied.setReadOnly(True)

        self.mn1groupbox2 = QGroupBox("자원")
        self.mn1grid2 = QGridLayout()
        self.mn1grid2.addWidget(self.mn1healthlabel, 0, 0)
        self.mn1grid2.addWidget(self.mn1healthlied, 0, 1)
        self.mn1grid2.addWidget(self.mn1reddicelabel, 0, 2)
        self.mn1grid2.addWidget(self.mn1reddicelied, 0, 3)
        self.mn1grid2.addWidget(self.mn1amountlabel, 0, 4)
        self.mn1grid2.addWidget(self.mn1manalabel, 1, 0)
        self.mn1grid2.addWidget(self.mn1manalied, 1, 1)
        self.mn1grid2.addWidget(self.mn1bluedicelabel, 1, 2)
        self.mn1grid2.addWidget(self.mn1bluedicelied, 1, 3)
        self.mn1grid2.addWidget(self.mn1amountlabel2, 1, 4)
        self.mn1grid2.addWidget(self.mn1actlabel, 2, 0)
        self.mn1grid2.addWidget(self.mn1actlied, 2, 1)
        self.mn1grid2.addWidget(self.mn1maxactlabel, 2, 2)
        self.mn1grid2.addWidget(self.mn1maxactlied, 2, 3)
        self.mn1grid2.addWidget(self.mn1amountlabel3, 2, 4)
        self.grid33 = QGridLayout()
        self.grid33.addWidget(self.mn1redrollresultlabel, 0, 0)
        self.grid33.addWidget(self.mn1redrollresultlied, 0, 1)
        self.grid33.addWidget(self.mn1bluerollresultlabel, 1, 0)
        self.grid33.addWidget(self.mn1bluerollresultlied, 1, 1)
        self.grid33.addWidget(self.mn1greenrollresultlabel, 2, 0)
        self.grid33.addWidget(self.mn1greenrollresultlied, 2, 1)

        self.vbox3 = QVBoxLayout()
        self.vbox3.addLayout(self.mn1grid2)
        self.vbox3.addLayout(self.grid33)
        self.mn1groupbox2.setLayout(self.vbox3)

        ##3rdgroup-1st part
        self.mn1spelluselistte = QTextBrowser(self)
        self.mn1groupbox3 = QGroupBox("<사용할 마법 대기열>")
        self.mn1vbox3 = QVBoxLayout()
        self.mn1vbox3.addWidget(self.mn1spelluselistte)
        self.mn1groupbox3.setLayout(self.mn1vbox3)

        ##2nd group-2st part
        self.mn1allturnbuffte = QTextBrowser(self)
        self.mn1turnbuffte = QTextBrowser(self)
        self.mn1actionbuffte = QTextBrowser(self)
        self.mn1grgroup1 = QGroupBox("<전투 부여 효과>")
        self.mn1grgroup2 = QGroupBox("<턴 부여 효과>")
        self.mn1grgroup3 = QGroupBox("<행동 부여 효과>")
        self.mn1groupbox4 = QGroupBox("<부여 효과>")
        self.mn1grgrid1 = QGridLayout()
        self.mn1grgrid2 = QGridLayout()
        self.mn1grgrid3 = QGridLayout()
        self.mn1vbox4 = QVBoxLayout()
        self.mn1grgrid1.addWidget(self.mn1allturnbuffte, 0, 0)
        self.mn1grgrid2.addWidget(self.mn1turnbuffte, 0, 0)
        self.mn1grgrid3.addWidget(self.mn1actionbuffte, 0, 0)
        self.mn1grgroup1.setLayout(self.mn1grgrid1)
        self.mn1grgroup2.setLayout(self.mn1grgrid2)
        self.mn1grgroup3.setLayout(self.mn1grgrid3)
        self.mn1vbox4.addWidget(self.mn1grgroup1)
        self.mn1vbox4.addWidget(self.mn1grgroup2)
        self.mn1vbox4.addWidget(self.mn1grgroup3)
        self.mn1groupbox4.setLayout(self.mn1vbox4)

        ##3rd group-3st part
        self.mn1attackte = QTextBrowser(self)
        self.mn1defencelied = QLineEdit(self)
        self.mn1defencelied.setReadOnly(True)
        self.mn1faultbtn = QPushButton("[회색이 되면 행동불능!]")

        self.mn1grgroup4 = QGroupBox("방어력")
        self.mn1grgroup5 = QGroupBox("공격대상/공격력")
        self.mn1grgrid4 = QGridLayout()
        self.mn1grgrid5 = QGridLayout()
        self.mn1grgrid4.addWidget(self.mn1defencelied, 0, 0)
        self.mn1grgrid5.addWidget(self.mn1attackte, 0, 0)
        self.mn1grgroup4.setLayout(self.mn1grgrid4)
        self.mn1grgroup5.setLayout(self.mn1grgrid5)
        self.mn1vbox5 = QVBoxLayout()
        self.mn1vbox5.addWidget(self.mn1faultbtn)
        self.mn1vbox5.addWidget(self.mn1grgroup4)
        self.mn1hbox5 = QHBoxLayout()
        self.mn1hbox5.addWidget(self.mn1grgroup5)
        self.mn1hbox5.addLayout(self.mn1vbox5)
        self.mn1groupbox5 = QGroupBox("방어력-공격력-행동불능여부")
        self.mn1groupbox5.setLayout(self.mn1hbox5)

        ##3rd group-main
        self.mn1maingroup2 = QGroupBox("적0")
        self.mn1namelied = QLineEdit(self)
        self.mn1namelied.setReadOnly(True)
        self.mn1namelabel = QLabel("적의 이름 : ")
        self.mn1hbox = QHBoxLayout()
        self.mn1hbox.addWidget(self.mn1namelabel)
        self.mn1hbox.addWidget((self.mn1namelied))
        self.mn1m2vbox = QVBoxLayout()
        self.mn1m2vbox.addLayout(self.mn1hbox)
        self.mn1m2vbox.addWidget(self.mn1groupbox2)
        self.mn1m2vbox.addWidget(self.mn1groupbox3)
        self.mn1m2vbox.addWidget(self.mn1groupbox4)
        self.mn1m2vbox.addWidget(self.mn1groupbox5)
        self.mn1maingroup2.setLayout(self.mn1m2vbox)








        ##4st group-1st part
        self.mn2healthlabel = QLabel("체력", self)
        self.mn2healthlied = QLineEdit(self)
        self.mn2reddicelabel = QLabel("(붉은 주사위", self)
        self.mn2reddicelied = QLineEdit(self)
        self.mn2amountlabel = QLabel("개)", self)

        self.mn2manalabel = QLabel("마력", self)
        self.mn2manalied = QLineEdit(self)
        self.mn2bluedicelabel = QLabel("(푸른 주사위", self)
        self.mn2bluedicelied = QLineEdit(self)
        self.mn2amountlabel2 = QLabel("개)", self)

        self.mn2actlabel = QLabel("행동력", self)
        self.mn2actlied = QLineEdit(self)
        self.mn2maxactlabel = QLabel("개 / ", self)
        self.mn2maxactlied = QLineEdit(self)
        self.mn2amountlabel3 = QLabel("개", self)

        self.mn2maxactlied.setReadOnly(True)
        self.mn2actlied.setReadOnly(True)
        self.mn2bluedicelied.setReadOnly(True)
        self.mn2healthlied.setReadOnly(True)
        self.mn2manalied.setReadOnly(True)
        self.mn2reddicelied.setReadOnly(True)

        self.mn2redrollresultlabel = QLabel("붉은 주사위 굴린 결과:")
        self.mn2bluerollresultlabel = QLabel("푸른 주사위 굴린 결과:")
        self.mn2greenrollresultlabel = QLabel("초록 주사위 굴린 결과:")
        self.mn2redrollresultlied = QLineEdit(self)
        self.mn2bluerollresultlied = QLineEdit(self)
        self.mn2greenrollresultlied = QLineEdit(self)
        self.mn2redrollresultlied.setReadOnly(True)
        self.mn2bluerollresultlied.setReadOnly(True)
        self.mn2greenrollresultlied.setReadOnly(True)

        self.mn2groupbox2 = QGroupBox("자원")
        self.mn2grid2 = QGridLayout()
        self.mn2grid2.addWidget(self.mn2healthlabel, 0, 0)
        self.mn2grid2.addWidget(self.mn2healthlied, 0, 1)
        self.mn2grid2.addWidget(self.mn2reddicelabel, 0, 2)
        self.mn2grid2.addWidget(self.mn2reddicelied, 0, 3)
        self.mn2grid2.addWidget(self.mn2amountlabel, 0, 4)
        self.mn2grid2.addWidget(self.mn2manalabel, 1, 0)
        self.mn2grid2.addWidget(self.mn2manalied, 1, 1)
        self.mn2grid2.addWidget(self.mn2bluedicelabel, 1, 2)
        self.mn2grid2.addWidget(self.mn2bluedicelied, 1, 3)
        self.mn2grid2.addWidget(self.mn2amountlabel2, 1, 4)
        self.mn2grid2.addWidget(self.mn2actlabel, 2, 0)
        self.mn2grid2.addWidget(self.mn2actlied, 2, 1)
        self.mn2grid2.addWidget(self.mn2maxactlabel, 2, 2)
        self.mn2grid2.addWidget(self.mn2maxactlied, 2, 3)
        self.mn2grid2.addWidget(self.mn2amountlabel3, 2, 4)
        self.grid44 = QGridLayout()
        self.grid44.addWidget(self.mn2redrollresultlabel, 0, 0)
        self.grid44.addWidget(self.mn2redrollresultlied, 0, 1)
        self.grid44.addWidget(self.mn2bluerollresultlabel, 1, 0)
        self.grid44.addWidget(self.mn2bluerollresultlied, 1, 1)
        self.grid44.addWidget(self.mn2greenrollresultlabel, 2, 0)
        self.grid44.addWidget(self.mn2greenrollresultlied, 2, 1)

        self.vbox4 = QVBoxLayout()
        self.vbox4.addLayout(self.mn2grid2)
        self.vbox4.addLayout(self.grid44)
        self.mn2groupbox2.setLayout(self.vbox4)

        ##4st group-1st part
        self.mn2spelluselistte = QTextBrowser(self)
        self.mn2groupbox3 = QGroupBox("<사용할 마법 대기열>")
        self.mn2vbox3 = QVBoxLayout()
        self.mn2vbox3.addWidget(self.mn2spelluselistte)
        self.mn2groupbox3.setLayout(self.mn2vbox3)

        ##4st group-2st part
        self.mn2allturnbuffte = QTextBrowser(self)
        self.mn2turnbuffte = QTextBrowser(self)
        self.mn2actionbuffte = QTextBrowser(self)
        self.mn2grgroup1 = QGroupBox("<전투 부여 효과>")
        self.mn2grgroup2 = QGroupBox("<턴 부여 효과>")
        self.mn2grgroup3 = QGroupBox("<행동 부여 효과>")
        self.mn2groupbox4 = QGroupBox("<부여 효과>")
        self.mn2grgrid1 = QGridLayout()
        self.mn2grgrid2 = QGridLayout()
        self.mn2grgrid3 = QGridLayout()
        self.mn2vbox4 = QVBoxLayout()
        self.mn2grgrid1.addWidget(self.mn2allturnbuffte, 0, 0)
        self.mn2grgrid2.addWidget(self.mn2turnbuffte, 0, 0)
        self.mn2grgrid3.addWidget(self.mn2actionbuffte, 0, 0)
        self.mn2grgroup1.setLayout(self.mn2grgrid1)
        self.mn2grgroup2.setLayout(self.mn2grgrid2)
        self.mn2grgroup3.setLayout(self.mn2grgrid3)
        self.mn2vbox4.addWidget(self.mn2grgroup1)
        self.mn2vbox4.addWidget(self.mn2grgroup2)
        self.mn2vbox4.addWidget(self.mn2grgroup3)
        self.mn2groupbox4.setLayout(self.mn2vbox4)

        ##4st group-3st part
        self.mn2attackte = QTextBrowser(self)
        self.mn2defencelied = QLineEdit(self)
        self.mn2defencelied.setReadOnly(True)
        self.mn2faultbtn = QPushButton("[회색이 되면 행동불능!]")

        self.mn2grgroup4 = QGroupBox("방어력")
        self.mn2grgroup5 = QGroupBox("공격대상/공격력")
        self.mn2grgrid4 = QGridLayout()
        self.mn2grgrid5 = QGridLayout()
        self.mn2grgrid4.addWidget(self.mn2defencelied, 0, 0)
        self.mn2grgrid5.addWidget(self.mn2attackte, 0, 0)
        self.mn2grgroup4.setLayout(self.mn2grgrid4)
        self.mn2grgroup5.setLayout(self.mn2grgrid5)
        self.mn2vbox5 = QVBoxLayout()
        self.mn2vbox5.addWidget(self.mn2faultbtn)
        self.mn2vbox5.addWidget(self.mn2grgroup4)
        self.mn2hbox5 = QHBoxLayout()
        self.mn2hbox5.addWidget(self.mn2grgroup5)
        self.mn2hbox5.addLayout(self.mn2vbox5)
        self.mn2groupbox5 = QGroupBox("방어력-공격력-행동불능여부")
        self.mn2groupbox5.setLayout(self.mn2hbox5)

        ##4st group-main
        self.mn2maingroup2 = QGroupBox("적1")
        self.mn2namelied = QLineEdit(self)
        self.mn2namelied.setReadOnly(True)
        self.mn2namelabel = QLabel("적의 이름 : ")
        self.mn2hbox = QHBoxLayout()
        self.mn2hbox.addWidget(self.mn2namelabel)
        self.mn2hbox.addWidget((self.mn2namelied))
        self.mn2m2vbox = QVBoxLayout()
        self.mn2m2vbox.addLayout(self.mn2hbox)
        self.mn2m2vbox.addWidget(self.mn2groupbox2)
        self.mn2m2vbox.addWidget(self.mn2groupbox3)
        self.mn2m2vbox.addWidget(self.mn2groupbox4)
        self.mn2m2vbox.addWidget(self.mn2groupbox5)
        self.mn2maingroup2.setLayout(self.mn2m2vbox)








        ##4st group-1st part
        self.mn3healthlabel = QLabel("체력", self)
        self.mn3healthlied = QLineEdit(self)
        self.mn3reddicelabel = QLabel("(붉은 주사위", self)
        self.mn3reddicelied = QLineEdit(self)
        self.mn3amountlabel = QLabel("개)", self)

        self.mn3manalabel = QLabel("마력", self)
        self.mn3manalied = QLineEdit(self)
        self.mn3bluedicelabel = QLabel("(푸른 주사위", self)
        self.mn3bluedicelied = QLineEdit(self)
        self.mn3amountlabel2 = QLabel("개)", self)

        self.mn3actlabel = QLabel("행동력", self)
        self.mn3actlied = QLineEdit(self)
        self.mn3maxactlabel = QLabel("개 / ", self)
        self.mn3maxactlied = QLineEdit(self)
        self.mn3amountlabel3 = QLabel("개", self)

        self.mn3maxactlied.setReadOnly(True)
        self.mn3actlied.setReadOnly(True)
        self.mn3bluedicelied.setReadOnly(True)
        self.mn3healthlied.setReadOnly(True)
        self.mn3manalied.setReadOnly(True)
        self.mn3reddicelied.setReadOnly(True)

        self.mn3redrollresultlabel = QLabel("붉은 주사위 굴린 결과:")
        self.mn3bluerollresultlabel = QLabel("푸른 주사위 굴린 결과:")
        self.mn3greenrollresultlabel = QLabel("초록 주사위 굴린 결과:")
        self.mn3redrollresultlied = QLineEdit(self)
        self.mn3bluerollresultlied = QLineEdit(self)
        self.mn3greenrollresultlied = QLineEdit(self)
        self.mn3redrollresultlied.setReadOnly(True)
        self.mn3bluerollresultlied.setReadOnly(True)
        self.mn3greenrollresultlied.setReadOnly(True)

        self.mn3groupbox2 = QGroupBox("자원")
        self.mn3grid2 = QGridLayout()
        self.mn3grid2.addWidget(self.mn3healthlabel, 0, 0)
        self.mn3grid2.addWidget(self.mn3healthlied, 0, 1)
        self.mn3grid2.addWidget(self.mn3reddicelabel, 0, 2)
        self.mn3grid2.addWidget(self.mn3reddicelied, 0, 3)
        self.mn3grid2.addWidget(self.mn3amountlabel, 0, 4)
        self.mn3grid2.addWidget(self.mn3manalabel, 1, 0)
        self.mn3grid2.addWidget(self.mn3manalied, 1, 1)
        self.mn3grid2.addWidget(self.mn3bluedicelabel, 1, 2)
        self.mn3grid2.addWidget(self.mn3bluedicelied, 1, 3)
        self.mn3grid2.addWidget(self.mn3amountlabel2, 1, 4)
        self.mn3grid2.addWidget(self.mn3actlabel, 2, 0)
        self.mn3grid2.addWidget(self.mn3actlied, 2, 1)
        self.mn3grid2.addWidget(self.mn3maxactlabel, 2, 2)
        self.mn3grid2.addWidget(self.mn3maxactlied, 2, 3)
        self.mn3grid2.addWidget(self.mn3amountlabel3, 2, 4)
        self.grid55 = QGridLayout()
        self.grid55.addWidget(self.mn3redrollresultlabel, 0, 0)
        self.grid55.addWidget(self.mn3redrollresultlied, 0, 1)
        self.grid55.addWidget(self.mn3bluerollresultlabel, 1, 0)
        self.grid55.addWidget(self.mn3bluerollresultlied, 1, 1)
        self.grid55.addWidget(self.mn3greenrollresultlabel, 2, 0)
        self.grid55.addWidget(self.mn3greenrollresultlied, 2, 1)

        self.vbox5 = QVBoxLayout()
        self.vbox5.addLayout(self.mn3grid2)
        self.vbox5.addLayout(self.grid55)
        self.mn3groupbox2.setLayout(self.vbox5)

        ##4st group-1st part
        self.mn3spelluselistte = QTextBrowser(self)
        self.mn3groupbox3 = QGroupBox("<사용할 마법 대기열>")
        self.mn3vbox3 = QVBoxLayout()
        self.mn3vbox3.addWidget(self.mn3spelluselistte)
        self.mn3groupbox3.setLayout(self.mn3vbox3)

        ##4st group-2st part
        self.mn3allturnbuffte = QTextBrowser(self)
        self.mn3turnbuffte = QTextBrowser(self)
        self.mn3actionbuffte = QTextBrowser(self)
        self.mn3grgroup1 = QGroupBox("<전투 부여 효과>")
        self.mn3grgroup2 = QGroupBox("<턴 부여 효과>")
        self.mn3grgroup3 = QGroupBox("<행동 부여 효과>")
        self.mn3groupbox4 = QGroupBox("<부여 효과>")
        self.mn3grgrid1 = QGridLayout()
        self.mn3grgrid2 = QGridLayout()
        self.mn3grgrid3 = QGridLayout()
        self.mn3vbox4 = QVBoxLayout()
        self.mn3grgrid1.addWidget(self.mn3allturnbuffte, 0, 0)
        self.mn3grgrid2.addWidget(self.mn3turnbuffte, 0, 0)
        self.mn3grgrid3.addWidget(self.mn3actionbuffte, 0, 0)
        self.mn3grgroup1.setLayout(self.mn3grgrid1)
        self.mn3grgroup2.setLayout(self.mn3grgrid2)
        self.mn3grgroup3.setLayout(self.mn3grgrid3)
        self.mn3vbox4.addWidget(self.mn3grgroup1)
        self.mn3vbox4.addWidget(self.mn3grgroup2)
        self.mn3vbox4.addWidget(self.mn3grgroup3)
        self.mn3groupbox4.setLayout(self.mn3vbox4)

        ##5st group-3st part
        self.mn3attackte = QTextBrowser(self)
        self.mn3defencelied = QLineEdit(self)
        self.mn3defencelied.setReadOnly(True)
        self.mn3faultbtn = QPushButton("[회색이 되면 행동불능!]")

        self.mn3grgroup4 = QGroupBox("방어력")
        self.mn3grgroup5 = QGroupBox("공격대상/공격력")
        self.mn3grgrid4 = QGridLayout()
        self.mn3grgrid5 = QGridLayout()
        self.mn3grgrid4.addWidget(self.mn3defencelied, 0, 0)
        self.mn3grgrid5.addWidget(self.mn3attackte, 0, 0)
        self.mn3grgroup4.setLayout(self.mn3grgrid4)
        self.mn3grgroup5.setLayout(self.mn3grgrid5)
        self.mn3vbox5 = QVBoxLayout()
        self.mn3vbox5.addWidget(self.mn3faultbtn)
        self.mn3vbox5.addWidget(self.mn3grgroup4)
        self.mn3hbox5 = QHBoxLayout()
        self.mn3hbox5.addWidget(self.mn3grgroup5)
        self.mn3hbox5.addLayout(self.mn3vbox5)
        self.mn3groupbox5 = QGroupBox("방어력-공격력-행동불능여부")
        self.mn3groupbox5.setLayout(self.mn3hbox5)

        ##5st group-main
        self.mn3maingroup2 = QGroupBox("적2")
        self.mn3namelied = QLineEdit(self)
        self.mn3namelied.setReadOnly(True)
        self.mn3namelabel = QLabel("적의 이름 : ")
        self.mn3hbox = QHBoxLayout()
        self.mn3hbox.addWidget(self.mn3namelabel)
        self.mn3hbox.addWidget((self.mn3namelied))
        self.mn3m2vbox = QVBoxLayout()
        self.mn3m2vbox.addLayout(self.mn3hbox)
        self.mn3m2vbox.addWidget(self.mn3groupbox2)
        self.mn3m2vbox.addWidget(self.mn3groupbox3)
        self.mn3m2vbox.addWidget(self.mn3groupbox4)
        self.mn3m2vbox.addWidget(self.mn3groupbox5)
        self.mn3maingroup2.setLayout(self.mn3m2vbox)


        #6st group

        # /result/
        self.reshealthlabel = QLabel("사용될 체력", self)
        self.reshealthlied = QLineEdit(self)
        self.resreddicelabel = QLabel("(붉은 주사위", self)
        self.resreddicelied = QLineEdit(self)
        self.resamountlabel = QLabel("개)", self)

        self.resmanalabel = QLabel("사용될 마력", self)
        self.resmanalied = QLineEdit(self)
        self.resbluedicelabel = QLabel("(푸른 주사위", self)
        self.resbluedicelied = QLineEdit(self)
        self.resamountlabel2 = QLabel("개)", self)

        self.resactlabel = QLabel("사용될 행동력", self)
        self.resactlied = QLineEdit(self)
        self.resmaxactlabel = QLabel("개 / ", self)
        self.resmaxactlied = QLineEdit(self)
        self.resamountlabel3 = QLabel("개", self)

        self.resmaxactlied.setReadOnly(True)
        self.resactlied.setReadOnly(True)
        self.resbluedicelied.setReadOnly(True)
        self.reshealthlied.setReadOnly(True)
        self.resmanalied.setReadOnly(True)
        self.resreddicelied.setReadOnly(True)

        self.resgroupbox2 = QGroupBox("사용될 자원")
        self.resgrid2 = QGridLayout()
        self.resgrid2.addWidget(self.reshealthlabel, 0, 0)
        self.resgrid2.addWidget(self.reshealthlied, 0, 1)
        self.resgrid2.addWidget(self.resreddicelabel, 0, 2)
        self.resgrid2.addWidget(self.resreddicelied, 0, 3)
        self.resgrid2.addWidget(self.resamountlabel, 0, 4)
        self.resgrid2.addWidget(self.resmanalabel, 1, 0)
        self.resgrid2.addWidget(self.resmanalied, 1, 1)
        self.resgrid2.addWidget(self.resbluedicelabel, 1, 2)
        self.resgrid2.addWidget(self.resbluedicelied, 1, 3)
        self.resgrid2.addWidget(self.resamountlabel2, 1, 4)
        self.resgrid2.addWidget(self.resactlabel, 2, 0)
        self.resgrid2.addWidget(self.resactlied, 2, 1)
        self.resgrid2.addWidget(self.resmaxactlabel, 2, 2)
        self.resgrid2.addWidget(self.resmaxactlied, 2, 3)
        self.resgrid2.addWidget(self.resamountlabel3, 2, 4)

        self.resvbox2 = QVBoxLayout()
        self.resvbox2.addLayout(self.resgrid2)
        self.resgroupbox2.setLayout(self.resvbox2)
        # /result/

        self.dicelistlied = QLineEdit(self)
        self.dicelistlied.setReadOnly(True)
        self.dicelistlabel = QLabel("<설명란>")
        self.bagte = QTextBrowser(self)

        self.moneylabel = QLabel("돈")
        self.moneylied = QLineEdit(self)
        self.moneylied.setReadOnly(True)
        self.specialbuffte = QTextBrowser()
        self.specialbufflabel = QLabel("특수 버프 리스트")
        self.gr6group = QGroupBox("중립 주사위 리스트:")
        self.gr6g2roup = QGroupBox("가방")

        self.gr6grid = QGridLayout()
        self.gr6g2rid = QGridLayout()

        self.gr6grid.addWidget(self.dicelistlabel)
        self.gr6grid.addWidget(self.dicelistlied)
        self.gr6g2rid.addWidget(self.bagte)
        self.gr6g2rid.addWidget(self.moneylabel)
        self.gr6g2rid.addWidget(self.moneylied)

        self.gr6group.setLayout(self.gr6grid)
        self.gr6g2roup.setLayout(self.gr6g2rid)

        self.groupbox6 = QGroupBox("기타 정보")
        self.vbox6 = QVBoxLayout()
        self.vbox6.addWidget(self.gr6group)
        self.vbox6.addWidget(self.resgroupbox2)
        self.vbox6.addWidget(self.gr6g2roup)

        self.vbox6.addWidget(self.specialbufflabel)
        self.vbox6.addWidget(self.specialbuffte)

        self.groupbox6.setLayout(self.vbox6)




        #mainbox
        self.vslabel = QLabel(" VS ")
        self.mhbox = QHBoxLayout()
        self.mhbox.addWidget(self.groupbox1,10)
        self.mhbox.addWidget(self.groupbox6,1)
        self.mhbox.addWidget(self.maingroup2,1)
        self.mhbox.addWidget((self.vslabel),1)
        self.mhbox.addWidget(self.mn1maingroup2,1)
        self.mhbox.addWidget(self.mn2maingroup2,1)
        self.mhbox.addWidget(self.mn3maingroup2,1)

        self.mvbox = QVBoxLayout()
        self.mvbox.addLayout(self.mhbox)

        self.setLayout(self.mvbox)




        self.btn.clicked.connect(self.h_inputstart)
        self.nextbtn.clicked.connect(self.h_printstart)

        self.setWindowTitle('QTextEdit')
        self.setGeometry(300, 300, 300, 200)
        self.show()


        #....print Area..........................................................................................

        hero = Character("hero", 60, 60, 3)
        hero.add_spell(BloodShield)
        hero.add_spell(BloodSpear)
        hero.add_spell(WeakenGas)
        hero.add_spell(RedPoisonSplay)
        hero.add_spell(CausingBleeding)

        hero.add_spell(ArcaneShield)
        hero.add_spell(ArcaneArrow)
        hero.add_spell(ArcaneAmplify)
        hero.add_spell(ManaBurst)
        hero.add_spell(Overflow)

        hero.add_spell(ThrowGreenDice)
        hero.add_spell(ManaCirculation)
        hero.add_spell(LowClassEarthSpiritsEmploy)

        hero.add_spell(OwnerKick)

        slime1 = Character("슬라임1", 15, 15, 3)
        slime2 = Character("슬라임2", 15, 15, 3)
        monsterlist = [slime1, slime2]

        for i in range(len(monsterlist)):
            monsterlist[i].add_spell(SlimeGuard)
            monsterlist[i].add_spell(SlimeJump)
            monsterlist[i].add_spell(SlimePowerJump)

        self.printt('주사위 마법사의 모험에 오신것을 환영합니다.')
        self.printt('작은 슬라임 이 전투를 걸어왔다!')
        self.printt('마법사의 붉은 피와 푸른 마나가 마력을 담은 주사위의 형상을 이루기 시작하였다.')
        self.printt('마법사의 두 눈은 상대의 체력과 기력/마나를 주사위의 형태로 파악해내기 시작하였다.')

        self.printt('')

        Store.Open_Store(hero, self)

        while (Fight.fight_end == False):
            monster_brainlist = [Slimebrain.slimebrain1, Slimebrain.slimebrain1]
            monster_availbrainlist = [Slimebrain.slimeavailbrain1, Slimebrain.slimeavailbrain1]
            Fight.big_fight(hero, monsterlist, monster_brainlist, monster_availbrainlist, self)
        self.printt('')

        self.printt('전투 보상: 1 붉은 마력 주사위, 5 푸른 마력 주사위.')
        hero.change_health(hero.health + 1 * Character.healthtodice,monsterlist,self)
        hero.change_mana(hero.mana.value + 5 * Character.manatodice,monsterlist,self)

        Store.Open_Store(hero, self)

        #########################################################################################################
        stone_golem = Character("스톤 골렘", 50, 30, 4)
        monsterlist = [stone_golem]

        for i in range(len(monsterlist)):
            monsterlist[i].add_spell(StoneGolemBoom)
            monsterlist[i].add_spell(StoneGolemWall)
            monsterlist[i].add_spell(StoneGolemPowerBoom)

        Fight.clear_all(hero, monsterlist, self)

        self.printt('')
        self.printt('강력한 스톤 골렘이 전투를 걸어왔다!')

        self.printt('')
        while (Fight.fight_end == False):
            monster_brainlist = [Stone_golembrain.stone_golembrain1]
            monster_availbrainlist = [Stone_golembrain.stone_golemavailbrain1]
            Fight.big_fight(hero, monsterlist, monster_brainlist, monster_availbrainlist, self)
        self.printt('')

        self.printt("개발자의 한마디: 베타 버전의 모든 몬스터를 잡았네요. 축하!")

        # ....print Area............................................................................................

    def printt(self, string, end=None):  # 딜레이가 있는 print. 단 sep와 end를 사용할 수 없다ㅠㅠㅠ
        if type(string) != type("abc"):
            string = str(string)

        self.h_printtimer(1)

        if end != None:
            print(string, end=end)
            self.te.insertPlainText(str(string))
        else:
            print(string)
            self.te.append(str(string))

        self.show()
        self.printallow = False

    def h_printtimer(self,i):
        while self.printallow == False:
            i += 1
            QtTest.QTest.qWait(10)

    def h_printstart(self):
        self.printallow = True

    def h_inputstart(self):

        if self.inputallow == True:
            self.h_inputvchange()

    def h_inputvchange(self):
        self.ttsig.inputsig.emit(self.li.text())
        self.li.clear()
        self.inputallow = False

    def inputt(self,string):
        self.printt(string)
        self.ttsig.inputsig.connect(self.h_inputslot)
        self.inputallow = True
        self.h_inputtimer(1)
        return self.inputvalue


    def h_inputslot(self,state):
        self.inputvalue = state

    def h_inputtimer(self, i):
        while self.inputallow == True:
            i += 1
            QtTest.QTest.qWait(10)



    #def h_aftertimer(self):
    #    print(self.inputvalue)



app = QApplication(sys.argv)
ex = MyApp()
sys.exit(app.exec_())
