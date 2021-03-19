class TextComparer:
    def __init__(self, url_list):
        self.url_list = url_list
        self.filenames = list()
    
    def download(self, url, filename):
        r = requests.get(url)
        if(r.status_code == 404):
            raise Exception('URL ' + url + " NOT FOUND")
        #print('',r.json()['url'])
        open('./downloads/' + filename + ".txt", 'wb').write(r.content)
        
    def multi_download_func(self, idx):
        try:
            filename = 'download_number_' + str(idx+1)
            self.download(self.url_list[idx], filename)
            self.filenames.append(filename)
        except:
            print('Could not download nr: ' + str(idx+1) + ', from URL: ' + self.url_list[idx])
        
    def multi_download(self):
        multithreading(self.multi_download_func, range(0,len(self.url_list)))
        
    def __iter__(self):
        self.iter_count = 0;
        return self
        
    def __next__(self):
        if self.iter_count < len(self.filenames):
            next = self.filenames[self.iter_count]
            self.iter_count += 1
            return next
        else:
            raise StopIteration
        
    def urllist_generator(self):
        num = 0
        while num < len(self.url_list):
            yield self.url_list[num]
            num += 1
        
    def avg_vowels(self, text):
        vowels = ['a', 'e', 'i', 'o', 'u', 'y']
        total_vowels_number = 0
        all_words = str(text).split(' ')
        for word in all_words:
            for letter in word:
                if str(letter).lower() in vowels:
                    total_vowels_number += 1
        avg_vowels_count = total_vowels_number/len(all_words)
        return avg_vowels_count
        
    def read_file(self, filename):
        filetext = open('./downloads/' + filename + '.txt', 'r').read()
        text_avg_vowels = self.avg_vowels(filetext)
        return filename, text_avg_vowels
    
    def hardest_read(self):
        hardest_read = {'File': 'No files to read', 'Score': 0}
        file_scores = multiprocessing(self.read_file, self.filenames)
        print(file_scores)
        for idx in range(0,len(file_scores)):
            if hardest_read['Score'] < file_scores[idx][1]:
                hardest_read['File'] = file_scores[idx][0]
                hardest_read['Score'] = file_scores[idx][1]
        return hardest_read['File'] + '.txt'