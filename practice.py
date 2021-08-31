import sys
sys.path.append('C:\\Users\\Pulkit\\AppData\\Local\\Programs\\Python\\Python38\\Lib\\site-packages')

import sublime
import sublime_plugin

from bs4 import BeautifulSoup
import urllib.request
import random





class GeeksCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        res = '/*\n'
        # connect to the gfg page of having 160+ top interview questions
        response = urllib.request.urlopen(
            'https://www.geeksforgeeks.org/must-do-coding-questions-for-companies-like-amazon-microsoft-adobe/')

    # parse the page using BeautifulSoup
        soup = BeautifulSoup(response.read(), 'html.parser')

        # We need to collect all the links in the page
        links = soup.findAll('a')

    # will store only the links of the problems
        valid_links = []

    # question problem links can be identified anc collected
        for link in links:
            if link.has_attr('href') and 'practice' in link['href'] and 'problems' in link['href']:
                valid_links.append(link['href'])

    # choose a random link
        random_link = random.choice(valid_links)
        # connect to the problem link
        response = urllib.request.urlopen(random_link)

        soup = BeautifulSoup(response.read(), 'html.parser')

        # find and store the tile of the question
        title = '# '+soup.find(class_='problem-tab__name').get_text().lstrip()+'\n\n'

    # find and store the question description and link
        question = soup.find(class_='problem-statement')

        res += title + question.get_text() + '\n\n'+random_link + '\n\n */\n\n'

        # to remove random carraige returns that we were getting
        res = res.replace('\r', '').split(' ')
        res1 = ''
        count = 0
        for r in res:
            if(count == 20):
                res1 += '\n'+r+' '
                count = 0
            else:
                res1 += r+' '
                count += 1

        response.close()

        self.view.insert(edit, 0, res1)


class codemodeCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        code = '#include <bits/stdc++.h>\n#define ll long long\nusing namespace std;\nll mod = 1e9+7 ;\n\n\nint main()\n{\n\n\t#ifndef ONLINE_JUDGE\n\tfreopen("input.txt","r",stdin);\n\tfreopen("output.txt","w",stdout);\n\t#endif\n\n\n\t//fast I/O\n\tios_base::sync_with_stdio(false);\n\tcin.tie(NULL);\n\n\n\tint testcases;\n\tcin>>testcases;\n\n\n\twhile(testcases--){\n\n\t\tlong long n,k;\n\t\tcin>>n;\n\t\tll arr[n];\n\t\tfor (int i = 0; i < n; ++i)\n\t\t{\n\t\t\tcin>>arr[i];\n\t\t}\n\n\t}\n  return 0;\n}'
        self.view.insert(edit, 0, code)
