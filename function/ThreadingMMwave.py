import threading
import time
import os
import sys


class MMwaveExperiment:
    def __init__(self, config_data):
        self.config_data = config_data
        # print(config_data)
        #時間戳紀錄
        self.experiment_time_result = None
        self.mmwave_time_result = None

        #是否執行完畢-flag
        self.is_mmwave_finish = False
        self.is_handle_finish = False

        
        #執行器配置(勿修改)
        self.handle_results = None
        self.set_time_out = config_data['set']['handle_time_out']  # 取樣頻率
        self.status = {
            'Experiment': "MMwave"
                       } #狀態輸出資訊



    def play_audio(self):
        pass
        # # 開始時間
        # start_time = time.time()
        # print(os.path.join(self.input_dir, self.play_filename))
        # # pygame.mixer.init()
        
        # # pygame.mixer.music.load(os.path.join(self.input_dir, self.play_filename))

        # # pygame.mixer.init()
        # # # 播放音樂
        # # pygame.mixer.music.play()

        # # # 等待音檔播放完畢
        # # while pygame.mixer.music.get_busy() == True:
        # #     continue

        # soundfile= os.path.join(self.input_dir, self.play_filename)
        # song=AudioSegment.from_wav(soundfile)
        # play(song)

        # # 結束時間
        # end_time = time.time()

        # self.play_time_result = start_time, end_time #設定本次時間點
        # self.is_play_finish = True #立flag

    def mmwave_record(self):
        pass
    
    def run_experiment(self):
        mmwave_thread = threading.Thread(target=self.mmwave_record, args=())

        self.experiment_time_result = time.time()
        mmwave_thread.start()

        mmwave_thread.join()


        self.process_results_debug()
        # 使用時一定要以物件使用，不可重複使用物件(宣告一個新的或繼承)


    
    def wait_for_processing(self):
        time_out = 0
        status = 200
        while self.is_mmwave_finish is False:
            time_out +=1
            print(f"wait for processing --- {time_out} / {self.set_time_out}")
            if time_out >= self.set_time_out:
                print("Timeout")
                status = 408 
                break
            time.sleep(1)  # 等待結果
        
        return status
    
    def handle_mmwave_time_result(self):
        try:
            mmwave_start, mmwave_end = self.mmwave_mmwave_result
            print(f"收集實驗時間差: {mmwave_end - mmwave_start}")
        except:
            print(f"mmwave sound fail")
   
   

    def process_results_debug(self):
        # 確保兩個執行緒都已經完成
        time_out = 0

        self.status['process_handle_results'] = self.wait_for_processing()

        # 取得結果
        self.handle_mmwave_time_result()
       

        # 建立一個字典來儲存你的變數
        results = {
            'experiment_time_result': self.experiment_time_result,
            'mmwave_result': self.mmwave_time_result,
            'is_mmwave_finish': self.is_mmwave_finish,


            'process_status': self.status
        }
        self.handle_results = results
        self.is_handle_finish = True #立flag


    def get_handle_results(self):
        return self.handle_results

    def get_is_handle_finish(self):
        return self.is_handle_finish
