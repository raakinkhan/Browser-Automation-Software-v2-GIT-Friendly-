import csv
import math
import multiprocessing
import threading
from tkinter import filedialog
from tkinter import *
import keyboard
import psutil
import time
import pyautogui
from cryptography.fernet import Fernet
import pyperclip
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
import base64
from PIL import Image, ImageGrab, ImageTk
import zlib
import datetime
import random
import string
import os
import io
import pickle
from tkinter import ttk
import customtkinter
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import hashlib

print("Welcome to Browser Automation Software !!!")

# count the number of processors in the current pc
ascii_str = string.ascii_letters
processor = multiprocessing.cpu_count()
error_status = 0
iteration_lock_for_quick_close = False
iteration_lock_for_built_in_func = False
lock_all_function = False
customtkinter.set_appearance_mode("Light")
wait_duration_in_main_unit = 0.1
screen_width, screen_height = pyautogui.size()
quality_control = 1
video_shoot_controler = 0
recorded_video_all_paths = []
paused = False
video_existence = 0
end_scrolling_value = 100
frame_count_limit = 30
visual_writing_index = 0

def check_and_self_construct():
    print("Checking Essential folder existence")
    date = time.localtime().tm_mday
    take_notes__normal_text___folder_existence = os.path.exists("All text files from TakeNote")
    browser_automation_software_stored_encrypted_file_folder_existence = os.path.exists(
        "Browser automation software stored encrypted files")
    browser_automation_important_cache_folder_existence = os.path.exists("Browser automation important cache files")
    folder_holding_file_folder_existence = os.path.exists("Folder Holding Files")
    images_for_Detection_folder_existence = os.path.exists("Images for Detection")
    # take_notes__encrypted_text___folder_existence = os.path.exists("Browser automation software stored encrypted files/Encrypted written notes/")
    to_do_list_folder_existence = os.path.exists("To-do list folder")
    doubly_hashed_master_key_file_existence = os.path.exists("Doubly hashed master key.enc")

    if take_notes__normal_text___folder_existence is False:
        print("Creating Take-notes TEXT folder ...")
        os.makedirs("All text files from TakeNote")
    if browser_automation_software_stored_encrypted_file_folder_existence is False:
        print("Creating Encrypter file folder ...")
        os.makedirs("Browser automation software stored encrypted files")
    else:
        enc_auth_details_folder_existence = os.path.exists(
            "Browser automation software stored encrypted files/Encrypted Authentication Details")
        enc_clipboards_folder_existence = os.path.exists(
            "Browser automation software stored encrypted files/encrypted clipboards")
        enc_screenrecords_folder_existence = os.path.exists(
            "Browser automation software stored encrypted files/Encrypted screenrecords")
        enc_screenshot_folder_existence = os.path.exists(
            "Browser automation software stored encrypted files/Encrypted screenshots")
        enc_written_notes_folder_existence = os.path.exists(
            "Browser automation software stored encrypted files/Encrypted written notes")
        enc_visual_descripter_folder_existence = os.path.exists(
            "Browser automation software stored encrypted files/Encrypted Visual descriptive writing")
        if enc_auth_details_folder_existence is False:
            print("Creating Authentication details folder ... ")
            os.makedirs("Browser automation software stored encrypted files/Encrypted Authentication Details")
        if enc_clipboards_folder_existence is False:
            print("Creating Clipboard folder ...")
            os.makedirs("Browser automation software stored encrypted files/encrypted clipboards")
            with open("Browser automation software stored encrypted files/encrypted clipboards/encrypted clipboards.enc", "a") as clipboard_file:
                clipboard_file.write(None)
        if enc_screenrecords_folder_existence is False:
            print("Creating Screen-records folder ... ")
            os.makedirs("Browser automation software stored encrypted files/Encrypted screenrecords")
        if enc_screenshot_folder_existence is False:
            print("Creating Screenshot folder ... ")
            os.makedirs("Browser automation software stored encrypted files/Encrypted screenshots")
        if enc_written_notes_folder_existence is False:
            print("Creating Encrypted Take notes folder ... ")
            os.makedirs("Browser automation software stored encrypted files/Encrypted written notes")
        if enc_visual_descripter_folder_existence is False:
            print("Creating Encrypted visual descripter folder ... ")
            os.makedirs("Browser automation software stored encrypted files/Encrypted Visual descriptive writing")
    if browser_automation_important_cache_folder_existence is False:
        print("Creating Cache folder ...")
        os.makedirs("Browser automation important cache files")
    else:
        image_instead_of_video_cache_data_folder_existence = os.path.exists("Browser automation important cache files/image instead of video cache data")
        modification_image_detection___folder___existence = os.path.exists("Browser automation important cache files/modification image detection list details")
        internet_and_time___graphing_data_file___existence = os.path.exists("Browser automation important cache files/internet and time   graphing list data   .pkl")
        quick_fill_file_existence = os.path.exists("Browser automation important cache files/Quick_fill.csv")
        internet_usage_file_existence = os.path.exists("Browser automation important cache files/Total internet usage today.pkl")
        if image_instead_of_video_cache_data_folder_existence is False:
            print("Creating Image instead of video cache data folder ...")
            os.makedirs("Browser automation important cache files/image instead of video cache data")
        if modification_image_detection___folder___existence is False:
            print("Creating image detection modification details folder ...")
            os.makedirs("Browser automation important cache files/modification image detection list details")
        if internet_and_time___graphing_data_file___existence is False:
            print("Creating internet and time, 'Graph details' ...")
            rewrite_dictionary = {
                "date": int(date),
                "Internet list": [0],  # internet used
                "time list": [0],
                "average internet rate": [0],
            }
            with open("Browser automation important cache files/internet and time   graphing list data   .pkl",
                      "wb") as refactored_file:  # total internet used, date
                pickle.dump(rewrite_dictionary, refactored_file)
        if quick_fill_file_existence is False:
            print("Creating Quick fill file ...")
            with open('Browser automation important cache files/Quick_fill.csv', 'w', newline='') as csvfile:
                quick_fill_file_writer = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                quick_fill_file_writer.writerow([0, 0])
        if internet_usage_file_existence is False:
            print("Creating Total internet usage file ...")
            rewrite_dictionary_ = {
                "date": int(date),
                "total internet used": 0,  # internet used
                "total time": 0,
            }
            with open("Browser automation important cache files/Total internet usage today.pkl",
                      "wb") as date_file:  # total internet used, date
                pickle.dump(rewrite_dictionary_, date_file)
    if folder_holding_file_folder_existence is False:
        print("Creating Folder holding file folder ...")
        os.makedirs("Folder Holding Files")
        folder_file_data = {
            "paths": []
        }
        with open("Folder Holding Files/General( B A S ).pkl", "wb") as reassign_folder_file:
            pickle.dump(folder_file_data, reassign_folder_file)
    if images_for_Detection_folder_existence is False:
        print("Creating Images for detection folder ...")
        os.makedirs("Images for Detection")
    # if take_notes__encrypted_text___folder_existence is False:
    #     print("Creating Take-notes Encrypted folder ...")
    if to_do_list_folder_existence is False:
        print("Creating To-do list folder ...")
        os.makedirs("To-do list folder")
    if doubly_hashed_master_key_file_existence is False:
        print("Creating Doubly Hashed Master Key file ...")
        with open("Doubly hashed master key.enc", "wb") as create_hashed_key_file:
            create_hashed_key_file.write(b"None")
    print("All Essential Folders EXISTS :D")

check_and_self_construct()
try:
    refactored_paths = os.listdir("Browser automation software stored encrypted files/Encrypted screenshots")
except:
    print("Please close and run he program again.")
    exit(0)
folder_file_name = "General( B A S ).pkl"
with open("Doubly hashed master key.enc", 'rb') as hashed_master_key__:  # initializing the matching master key
    matching_key_hashed = hashed_master_key__.read()

def reset_entry_fields_completely():
    # Resets all value in entry fields
    internet_limit_Entry.delete(0, "end")
    time_limit_Entry.delete(0, "end")



def convert_data():
    # Conversion function - converts Giga bytes to Mega bytes and Minutes to Seconds
    converted_mb = (int(internet_limit_Entry.get()) * 1024)

    internet_limit_Entry.delete(0, "end")
    internet_limit_Entry.insert(0, int(converted_mb))


def convert_time():
    # Conversion function - converts Giga bytes to Mega bytes and Minutes to Seconds
    converted_min = (int(time_limit_Entry.get()) * 60)
    time_limit_Entry.delete(0, "end")
    time_limit_Entry.insert(0, int(converted_min))

def read_quick_fill():
    # reads the quick fill
    reset_entry_fields_completely()
    with open('Browser automation important cache files/Quick_fill.csv', newline='') as csvfile:
        quick_fill_file_reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in quick_fill_file_reader:
            internet_limit_Entry.insert(0, int(row[0]))
            time_limit_Entry.insert(0, int(row[1]))


def overwrite_quick_fill():
    # writes the quick fill
    with open('Browser automation important cache files/Quick_fill.csv', 'w', newline='') as csvfile:
        quick_fill_file_writer = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        quick_fill_file_writer.writerow([internet_limit_Entry.get(), time_limit_Entry.get()])


def generate_username_and_copy():
    List_of_Random_first_names = ["Jhon", "Jhonny", "Jacob", "Jack", "Michael", "Joseph", "Benjamin", "Anthony", "Andrew", "Liam", "Oliver", "James", "Robert", "Daniel", "Ryan", "Rocky", "Matt", "Salman", "Omar", "Sattar", "Ram", "Lester", "Franklin", "Shing", "xiu"]
    List_of_Random_second_names = ["Christ", "Khan", "kiyosaki", "kausari", "winstor", "jinnah", "bond", "tate", "hood", "kumar", "ahmed", "kaaka", "Shah", "Traver", "Frank", "jonas", "Taj"]
    Random_number = str(random.randrange(1000, 10000))
    random_first_name = random.choice(List_of_Random_first_names)
    random_second_name = random.choice(List_of_Random_second_names)
    username = random_first_name+"_"+random_second_name+Random_number
    pyperclip.copy(username)


def generate_password():
    all_letters = string.ascii_letters+string.digits+string.punctuation
    random_string = ""
    for random_hash in range(20):
        random_choice = random.choice(all_letters)
        random_string+=str(random_choice)
    pyperclip.copy(random_string)


def Quick_copy_from_entry():
    global Quick_copy_Entry
    text_ = str(Quick_copy_Entry.get())
    if text_ != "":
        if text_.isspace() is False:
            pyperclip.copy(text_)


def grant_time():
    global granting_time_or_internet_entry_field, time_limit_future_bind
    granting_time_in_seconds = int(granting_time_or_internet_entry_field.get())
    time_limit_future_bind += granting_time_in_seconds
    print("Successfully granted ", granting_time_in_seconds, " Seconds")

def grant_data():
    global data_grant_list
    granting_data_in_mb = float(granting_time_or_internet_entry_field.get())
    print(granting_data_in_mb)
    data_grant_list.append(granting_data_in_mb)
    print(data_grant_list)
    print("Successfully granted", granting_data_in_mb, "MB")



def pop_up_analysing_window():  # analysis window shows all necessary monitoring values in a particular window
    global analysis_window
    global internet_label, time_label
    global internet_label_show_values, time_label_show_values, ram_usage_value_show_label, cpu_usage_show_values_label, avg_internet_show_values_label, internet_finish_show_prediction_values_label, granting_time_or_internet_entry_field
    # analysis window
    # --- All analysis window in built configuration attributes ---
    analysis_window = Toplevel(Input_Window)
    analysis_window.title("Monitoring")
    # --- All analysis window Frames ---
    main_monitor_values_frame = LabelFrame(analysis_window, text=" Monitoring ", font=("Courier", 15, "bold"))
    main_monitor_values_frame.pack(anchor=CENTER)
    in_built_functions_frame = LabelFrame(analysis_window, text=" In-Built Functions", font=("Courier", 15, "bold"), padx=100, pady=15)
    in_built_functions_frame.pack(anchor=CENTER)
    # --- All analysis widow widgets ---
    internet_label = Label(main_monitor_values_frame, text="Data Consumed :                                          ", font=("Arial", 15), pady=10, padx=20, foreground="darkblue")
    internet_label.grid(row=0, column=0)
    time_label = Label(main_monitor_values_frame, text="Time Consumed :                                          ", font=("Arial", 15), pady=10, padx=20, foreground="darkblue")
    time_label.grid(row=1, column=0)
    internet_label_show_values = Label(main_monitor_values_frame, text="Error", font=("Times", 15, "bold"), pady=10,
                                       padx=20)
    internet_label_show_values.grid(row=0, column=1)
    time_label_show_values = Label(main_monitor_values_frame, text="Error", font=("Times", 15, "bold"), pady=10, padx=20)
    time_label_show_values.grid(row=1, column=1)
    ram_usage_label = Label(main_monitor_values_frame, text="Memory usage :                                            ", font=("Arial", 15), pady=10, padx=20, foreground="darkred")
    ram_usage_label.grid(row=4, column=0)
    ram_usage_value_show_label = Label(main_monitor_values_frame, text="Error", font=("Times", 15, "bold"), pady=10, padx=20)
    ram_usage_value_show_label.grid(row=4, column=1)
    avg_internet_use_label = Label(main_monitor_values_frame, text="Data Consumed Per Second :                      ", font=("Arial", 15), pady=10, padx=20, foreground="purple")
    avg_internet_use_label.grid(row=2, column=0)
    avg_internet_show_values_label = Label(main_monitor_values_frame, text="Error", font=("Times", 15, "bold"), pady=10, padx=20)
    avg_internet_show_values_label.grid(row=2, column=1)
    internet_finish_prediction_label = Label(main_monitor_values_frame, text="Time predicted For Data To Be Exhausted : ",
                                   font=("Arial", 15), pady=10, padx=20, foreground="purple")
    internet_finish_prediction_label.grid(row=3, column=0)
    internet_finish_show_prediction_values_label = Label(main_monitor_values_frame, text="Error",
                                           font=("Times", 15, "bold"), pady=10, padx=20)
    internet_finish_show_prediction_values_label.grid(row=3, column=1)
    # ========================================================================= #
    Generate_username_button = customtkinter.CTkButton(in_built_functions_frame, text="Generate Username", font=("Arial", 13, "bold"), command=generate_username_and_copy)
    Generate_username_button.grid(row=0, column=0, padx=4)
    Generate_Password_button = customtkinter.CTkButton(in_built_functions_frame, text="Generate Password",
                                                       font=("Arial", 13, "bold"), command=generate_password)
    Generate_Password_button.grid(row=0, column=1, padx=4)


    granting_time_or_internet_entry_field = customtkinter.CTkEntry(in_built_functions_frame, font=("Courier", 15, "bold"), corner_radius=50, width=150, placeholder_text="Integer")
    granting_time_or_internet_entry_field.grid(row=2, column=0, pady=4)

    granting_time = customtkinter.CTkButton(in_built_functions_frame, text="Grant time",
                                                font=("Arial", 13, "bold"), command=grant_time)
    granting_time.grid(row=2, column=1, padx=4, pady=4)

    granting_internet = customtkinter.CTkButton(in_built_functions_frame, text="Grant Internet",
                                            font=("Arial", 13, "bold"), command=grant_data)
    granting_internet.grid(row=2, column=2, padx=4, pady=4)




def update_show_values_column(internet_value, time_value, avg_internet_value, predicted_internet_finish_time):  # updates labels in analysis window
    global internet_label_show_values, time_label_show_values, analysis_window, ram_usage_value_show_label, avg_internet_show_values_label, internet_finish_show_prediction_values_label, min_average_internet_distribution, avg_internet
    if analysis_window.winfo_exists() == 1:
        internet_label_show_values.config(text=str(internet_value))
        time_label_show_values.config(text=time_value)
        ram_usage_value_show_label.config(text=(psutil.virtual_memory().percent, "%"))
        if avg_internet <= min_average_internet_distribution:
            color_code_avg_internet_label = "green"
        else:
            color_code_avg_internet_label = "black"

        if predicted_time_for_internet_usage == "Infinite":
            color_code_internet_prediction_finish = "black"
        elif float(predicted_time_for_internet_usage) >= time_value:
            color_code_internet_prediction_finish = "green"
        else:
            color_code_internet_prediction_finish = "black"
        avg_internet_show_values_label.config(text=("{:.5}".format(avg_internet_value)+" / sec"), fg=color_code_avg_internet_label)
        internet_finish_show_prediction_values_label.config(text=(predicted_internet_finish_time+" seconds"), fg=color_code_internet_prediction_finish)


def key_derive():
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,  # 32 bytes for Fernet key
        salt=b'hash crack',
        iterations=100000,  # You can adjust the number of iterations
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive((encryption_key_Entry.get()).encode()))
    return key


def __run__main___():  # all threads, analysis window runs from here
    global prev_bytes_init_start_internet_sent, prev_bytes_init_start_internet_received, time_limit_future_bind, analysis_window, encrypter, key, matching_key_hashed, data_grant_list
    pop_up_analysing_window()
    init_start_data = psutil.net_io_counters()
    prev_bytes_init_start_internet_sent = init_start_data.bytes_sent
    prev_bytes_init_start_internet_received = init_start_data.bytes_recv
    time_limit_future_bind_calculation()
    key = key_derive()
    data_grant_list = [0]
    if double_encryption_key_generator(value=key.decode()) == matching_key_hashed:
        encrypter_key = key  # initialising encrypter
        encrypter = Fernet(encrypter_key)
        if analysis_window.winfo_exists() == 1:
            thread1 = threading.Thread(target=main_process_unit, daemon=True)
            thread1.start()



def total_internet_been_used(init_start_data_sent, init_start_data_recv):  # calculates the internet used
    try:
        net_io = psutil.net_io_counters()
        data_sent_mb = (net_io.bytes_sent - init_start_data_sent) / (1024 * 1024)
        data_received_mb = (net_io.bytes_recv - init_start_data_recv) / (1024 * 1024)
        # print("data sent:", data_sent_mb, "data received", data_received_mb)
        if data_received_mb < 0:
            data_sent_mb = 0
            data_received_mb = 0
        if data_sent_mb < 0:
            data_sent_mb = 0
            data_received_mb = 0
        total_data_used_mb = (data_sent_mb + data_received_mb)
        return total_data_used_mb
    except psutil.Error as e:
        print(f"Error: {e}")
        return 0.0


def check_internet(current_internet):  # checks if internet limit is reached or not
    global data_grant_list
    finish_internet_limit = float(internet_limit_Entry.get()) + sum(data_grant_list)
    # print(finish_internet_limit)
    if current_internet >= finish_internet_limit:
        print("Internet Limit reached")
        analysis_window.destroy()
        quick_close_current_window()


def current_total_time_in_seconds():  # calculates the current time in seconds
    current_time = time.localtime()
    current_second = current_time.tm_sec
    current_min_in_seconds = current_time.tm_min * 60
    current_hour_in_seconds = current_time.tm_hour * 3600
    time_in_sec = (current_second + current_min_in_seconds + current_hour_in_seconds)
    return time_in_sec


def time_limit_future_bind_calculation():  # calculates the time limit in seconds
    global time_limit_future_bind, limit_in_seconds
    limit_in_seconds = time_limit_Entry.get()
    current_time_in_seconds = current_total_time_in_seconds()
    time_limit_future_bind = (int(current_time_in_seconds) + int(limit_in_seconds))
    return time_limit_future_bind


def time_used_check(current_time):  # checks whether the time limit is used or not
    global analysis_window
    global time_limit_future_bind
    global limit_in_seconds
    if current_time >= time_limit_future_bind:
        print("Time Limit reached")
        analysis_window.destroy()
        quick_close_current_window()


def quick_close_current_window():  # closes google window by ctrl + w hotkey
    global option_box_var
    decision = str(option_box_var.get())
    if decision == "Chrome & Edge":
        pyautogui.keyDown("ctrl")
        pyautogui.press("w")
        pyautogui.keyUp("ctrl")
    elif decision == "Bluestacks5":
        pyautogui.keyDown("ctrl")
        pyautogui.keyDown("shift")
        pyautogui.press("X")
        pyautogui.keyUp("shift")
        pyautogui.keyUp("ctrl")
    elif decision == "Active Window":
        pyautogui.keyDown("alt")
        pyautogui.press("f4")
        pyautogui.keyUp("alt")
    elif decision == "Only Warn":
        pyautogui.keyDown("win")
        pyautogui.press("m")
        pyautogui.keyUp("win")
        warning_window = Toplevel(Input_Window)
        warning_window.title("WARNING")
        # You have reached your limit
        warning_window.minsize(width=800, height=80)
        warning_window.maxsize(width=800, height=80)
        Label(warning_window, text="! You have reached your limits !", font=("Courier", 25, "bold"),
              fg="red2").pack(anchor="center", pady=10)
    elif decision == "Minimize":
        pyautogui.keyDown("win")
        pyautogui.press("m")
        pyautogui.keyUp("win")


def encryption_of_clipboards(value):
    global encrypter
    cipher_value = encrypter.encrypt(value.encode())
    # print(cipher_value.decode())
    return cipher_value.decode()


def decryption_of_clipboards(value):
    global matching_key_hashed
    try:
        key = key_derive()
        if double_encryption_key_generator(value=(key.decode())) == matching_key_hashed:
            decryption_key = key
            decrypter = Fernet(decryption_key)
            decrypted_value = decrypter.decrypt(value.encode())
            return decrypted_value.decode()
    except:
            print("Error: some error while decrypting")


def clipboard_detect_and_encrypt():
    copied___ = str(pyperclip.paste())
    if not copied___.isspace():
        encrypted_clipboard = encryption_of_clipboards(value=copied___)
        clipboard_save_encrypted(values=encrypted_clipboard)
        # decryption(encrypted_clipboard.decode())


def clipboard_save_encrypted(values):
    with open("Browser automation software stored encrypted files/encrypted clipboards/encrypted clipboards.enc", 'a') as encryption_store:
        encryption_store.write(values)
        encryption_store.write("\n")


def decrypt_only_limit_iteration_clipboard():
    global decrypt_and_show_window, decrypt_and_show_list, values_in_list, Lines, init_line_decrypter_counter, value_of_lazy_loading_clipboards_entry
    iteration_limit = value_of_lazy_loading_clipboards_entry.get()
    for line_by_line in range(int(iteration_limit)):
        if init_line_decrypter_counter > len(Lines):
            break
        elif init_line_decrypter_counter < len(Lines):
            current_line = Lines[init_line_decrypter_counter]
            decrypted_value = decryption_of_clipboards(value=current_line)
            values_in_list.append(decrypted_value)
            decrypted_value_with_index = ("   " + str(init_line_decrypter_counter) + "   :   " + decrypted_value)
            if decrypt_and_show_window.winfo_exists() == 1:
                decrypt_and_show_list.insert(END, decrypted_value_with_index)
            init_line_decrypter_counter += 1


def clipboard_read_file_line_by_line():
    global decrypt_and_show_window, decrypt_and_show_list, values_in_list, Lines, init_line_decrypter_counter, value_of_lazy_loading_clipboards_entry
    values_in_list = []
    init_line_decrypter_counter = 0
    try:
        with open('Browser automation software stored encrypted files/encrypted clipboards/encrypted clipboards.enc', 'r') as read_encrypted_values:
            Lines = read_encrypted_values.readlines()
            decrypt_only_limit_iteration_clipboard()
    except:
        print("Error: Couldn't read the encrypted Clipboard file")


def delete_clipboard_and_refactor_clipboard_items(lower_limit, upper_limit):
    if lower_limit >= 0:
        actual_lower_limit = int(lower_limit)
        actual_upper_limit = int(upper_limit)+1

        with open('Browser automation software stored encrypted files/encrypted clipboards/encrypted clipboards.enc',
                  'r') as read_encrypted_values:
            all_lines_present = read_encrypted_values.readlines()
            # print(all_lines_present)

        # Delete lines within the specified range
        del all_lines_present[actual_lower_limit:actual_upper_limit]

        with open('Browser automation software stored encrypted files/encrypted clipboards/encrypted clipboards.enc',
                  'w') as over_write_encrypted_file:
            for line in all_lines_present:
                over_write_encrypted_file.write(line)

            # print(len(all_lines_present))


# Call the function with lower and upper limits

def get_values_from_entry_fields_for_deletion():
    global range_of_clipboards_to_delete_entry, decrypt_and_show_window
    value = range_of_clipboards_to_delete_entry.get()
    try:
        for ik in range(len(value)):
            if value[ik] == "-":
                lower_L = int(value[0:ik])
                upper_L = int(value[(ik+1):])
                # print(lower_L, upper_L)
        if lower_L <= upper_L:
            delete_clipboard_and_refactor_clipboard_items(lower_limit=lower_L, upper_limit=upper_L)
            decrypt_and_show_window.destroy()
            pop_up_decrypt_and_show_clipboards()
    except:
        print("Error: Invalid_entry or No Hyphen provided")
        range_of_clipboards_to_delete_entry.delete(0, "end")


def all_function_inside(modes):  # key = UeD_UsABDSt1BZoqU0lPTgkHJ-NWQrkcnKXFdGOLHuQ=, password_generated_key = 3BgensD03_XZlPSI3j5mCn4ZHBM3t2vmi-xmGLXFlpc=
    global iteration_lock_for_quick_close, lock_all_function, X1, Y1, state_of_the_Website_text, srX2, srY2
    if lock_all_function is False:
        if modes == 0:
            lock_all_function = True
            clipboard_detect_and_encrypt()
            lock_all_function = False
        if modes == 1:
            lock_all_function = True
            X2, Y2 = pyautogui.position()
            # print(X2, Y2)
            get_screenshot_compress_it_and_encrypt_it_and_send_those_bytes(x1=X1, y1=Y1, x2=X2, y2=Y2)
            # screenshot and encrypt functions over here
            lock_all_function = False








def on_key_event_for_quick_close(e):  # on key pressed do particular event
    global iteration_lock_for_quick_close, lock_all_function, X1, Y1, login_username, login_password, screenrecord_initializer_window, srX2, srY2, video_shoot_controler
    # ! problem ! - if I press for a second also it iterates 50 to 100 times
    if e.event_type == keyboard.KEY_DOWN:
        if iteration_lock_for_quick_close is False:
            if e.name == "tab":  # quick close
                quick_close_current_window()
            elif e.name == "q":  # copy clipboard
                thread = threading.Thread(target=all_function_inside, args=[0], daemon=True)
                thread.run()
            elif e.name == "o":  #  initial screenshot pos
                X1, Y1 = pyautogui.position()
                # print(X1, Y1)
                lock_all_function = False
            elif e.name == "*":  #  screenshot
                thread = threading.Thread(target=all_function_inside, args=[1], daemon=True)
                thread.run()
                lock_all_function = False
            elif e.name == "u":  #  detects the username image
                detect_and_click_on_username_image_and_enter_username_name()
            elif e.name == "p":  #  detects the password image
                detect_and_click_on_password_image_and_enter_password_name()
            elif e.name == "w":  #  detects the website so n so image
                detect_and_click_on_website_image_and_enter_website_name()
            elif e.name == "`":  #  deactivates the annoying detection, when only switched on
                deactivate_detection__image_auth__()
            # add all in built functions by key calls over here... reduces the memory usage
            iteration_lock_for_quick_close = True
    if e.event_type == keyboard.KEY_UP:
        iteration_lock_for_quick_close = False


def authentication_encrypter(L_username, L_password):
    global encrypted_login_username, encrypted_login_password
    encrypter = Fernet(key_derive())
    encrypted_login_username = encrypter.encrypt(L_username.encode())
    encrypted_login_password = encrypter.encrypt(L_password.encode())


def authentication_save_log_in_data_using_clipboard():
    global encrypted_login_username, encrypted_login_password
    secure_login_data = {
        "website": "None",
        "username": encrypted_login_username,
        "password": encrypted_login_password,
    }
    curr_time = time.localtime()
    curr_clock = time.strftime("%H-%M-%S", curr_time)
    time_tag_file_name_format = str(datetime.date.today()) + "-" + str(curr_clock)
    file_name = "Authentication details on "+time_tag_file_name_format+".pkl"
    with open("Browser automation software stored encrypted files//Encrypted Authentication Details//"+file_name, "wb") as enc_file_authe:
        pickle.dump(secure_login_data, enc_file_authe)


def get_lazy_load_from_entry_field_and_decrypt_authentication_Details():
    global lazy_load_authentication_details_entry
    lazy_load_value = int(lazy_load_authentication_details_entry.get())
    decrypt_and_show_the_authentication_details_with_lazy_load_values(lazy_load_value=lazy_load_value)


def get_index_value_from_entry_field_and_delete_the_authentication_details():
    global authentication_folder_list_of_all_files, delete_authentication_details_entry, Authentication_displayer
    deletion_file = authentication_folder_list_of_all_files[int(delete_authentication_details_entry.get())]
    os.remove("Browser automation software stored encrypted files/Encrypted Authentication Details/"+deletion_file)
    modification_image_detection_file_name = authentication_folder_list_of_all_files[int(delete_authentication_details_entry.get())]
    refactored_detection_File_name = modification_image_detection_file_name[0:-4] + " ( B A S ) ( Image detection data ).pkl"
    modification_image_detection_file_name = "Browser automation important cache files/modification image detection list details/" + refactored_detection_File_name
    os.remove(modification_image_detection_file_name)
    Authentication_displayer.destroy()
    pop_up_authentication_details_decrypter()


def add_authentication_from_entries():
    global website_entry_field_of_authentication_details, username_entry_field_of_authentication_details, password_entry_field_of_authentication_details
    global authentication_folder_list_of_all_files, encrypted_login_username, encrypted_login_password, Authentication_displayer
    the_username = str(username_entry_field_of_authentication_details.get())
    the_password = str(password_entry_field_of_authentication_details.get())
    the_website = str(website_entry_field_of_authentication_details.get())
    authentication_encrypter(L_username=the_username, L_password=the_password)
    secure_login_data = {
        "website": the_website,
        "username": encrypted_login_username,
        "password": encrypted_login_password,
    }
    curr_time = time.localtime()
    curr_clock = time.strftime("%H-%M-%S", curr_time)
    time_tag_file_name_format = str(datetime.date.today()) + "-" + str(curr_clock)
    file_name = "Authentication details on " + time_tag_file_name_format + ".pkl"
    with open("Browser automation software stored encrypted files//Encrypted Authentication Details//" + file_name,
              "wb") as enc_file_authe:
        pickle.dump(secure_login_data, enc_file_authe)
    Authentication_displayer.destroy()
    pop_up_authentication_details_decrypter()


def edit_authentication_details_from_entries():
    global website_entry_field_of_authentication_details, username_entry_field_of_authentication_details, password_entry_field_of_authentication_details, index_entry_field_of_authentication_Details
    global authentication_folder_list_of_all_files, encrypted_login_username, encrypted_login_password, Authentication_displayer
    the_username = str(username_entry_field_of_authentication_details.get())
    the_password = str(password_entry_field_of_authentication_details.get())
    the_website = str(website_entry_field_of_authentication_details.get())
    try:
        the_index = int(index_entry_field_of_authentication_Details.get())
        with open(("Browser automation software stored encrypted files/Encrypted Authentication Details/" +
                   authentication_folder_list_of_all_files[the_index]),
                  "rb") as fn:
            authentication_file_details = pickle.load(fn)
        if str(the_index).isnumeric() is True:
                if the_username == "-":
                    enc_username = authentication_file_details["username"]
                    dec_username = authentication_decrypter(value=enc_username)
                    the_username = dec_username
                if the_password == "-":
                    enc_password = authentication_file_details["password"]
                    dec_password = authentication_decrypter(value=enc_password)
                    the_password = dec_password
                if the_website == "-":
                    the_website = authentication_file_details["website"]
                authentication_encrypter(L_username=the_username, L_password=the_password)
                secure_login_data = {
                    "website": the_website,
                    "username": encrypted_login_username,
                    "password": encrypted_login_password,
                }
                with open("Browser automation software stored encrypted files/Encrypted Authentication Details/"+authentication_folder_list_of_all_files[int(the_index)], "wb") as edit_file:
                    pickle.dump(secure_login_data, edit_file)
                Authentication_displayer.destroy()
                pop_up_authentication_details_decrypter()
        else:
            print("Error: Index not filled Properly.")
            username_entry_field_of_authentication_details.delete(0, END)
            password_entry_field_of_authentication_details.delete(0, END)
            website_entry_field_of_authentication_details.delete(0, END)
            index_entry_field_of_authentication_Details.delete(0, END)
    except:
        print("Error: Index not filled Properly.")
        username_entry_field_of_authentication_details.delete(0, END)
        password_entry_field_of_authentication_details.delete(0, END)
        website_entry_field_of_authentication_details.delete(0, END)
        index_entry_field_of_authentication_Details.delete(0, END)




def get_username_from_index():
    global use_authentication_details_entry, authentication_folder_list_of_all_files
    with open(("Browser automation software stored encrypted files/Encrypted Authentication Details/" + authentication_folder_list_of_all_files[int(use_authentication_details_entry.get())]),
              "rb") as fn:
        auth_file = pickle.load(fn)
    enc_username = auth_file["username"]
    dec_username = authentication_decrypter(value=enc_username)
    pyperclip.copy(str(dec_username))


def get_password_from_index():
    global use_authentication_details_entry, authentication_folder_list_of_all_files
    with open(("Browser automation software stored encrypted files/Encrypted Authentication Details/" + authentication_folder_list_of_all_files[int(use_authentication_details_entry.get())]),
              "rb") as fn:
        auth_file = pickle.load(fn)
    enc_password = auth_file["password"]
    dec_password = authentication_decrypter(value=enc_password)
    pyperclip.copy(str(dec_password))


def get_website_from_index():
    global use_authentication_details_entry, authentication_folder_list_of_all_files
    with open(("Browser automation software stored encrypted files/Encrypted Authentication Details/" +
               authentication_folder_list_of_all_files[int(use_authentication_details_entry.get())]),
              "rb") as fn:
        auth_file = pickle.load(fn)
        website = auth_file["website"]
    pyperclip.copy(str(website))


def ctrl_v_event_listener(event):
    global automatic_switch_lock
    global Authentication_displayer
    if event.event_type == keyboard.KEY_DOWN and event.name == "v" and keyboard.is_pressed("ctrl"):
        get_password_from_index()
        keyboard.unhook(ctrl_v_event_listener)
        automatic_switch_lock = False


def automatic_switch():
    global automatic_switch_lock
    global Authentication_displayer
    get_username_from_index()
    if automatic_switch_lock == False:
        if Authentication_displayer.winfo_exists() == 1:
            keyboard.hook(ctrl_v_event_listener)
            automatic_switch_lock = True
        if Authentication_displayer.winfo_exists() == 0:
            keyboard.unhook(ctrl_v_event_listener)
            automatic_switch_lock = False


def pop_up_authentication_details_decrypter():
    global automatic_switch_lock
    global Authentication_displayer, authentication_folder_list_of_all_files, authentication_tree_view, lazy_load_remember_value, lazy_load_authentication_details_entry, delete_authentication_details_entry, edit_authentication_details_entry, add_authentication_details_entry, use_authentication_details_entry, index_entry_field_of_authentication_Details, index_of_the_detection___which_one
    global website_entry_field_of_authentication_details, username_entry_field_of_authentication_details, password_entry_field_of_authentication_details
    if matching_key_hashed == double_encryption_key_generator(value=(double_encryption_key_generator(value=encryption_key_Entry.get())).decode()):
        Authentication_displayer = Toplevel(Input_Window)
        Authentication_displayer.title("Authentication Details")
        Authentication_displayer.minsize(width=1285, height=510)
        Authentication_displayer.maxsize(width=1285, height=510)
        automatic_switch_lock = False
        authentication_operations_frame = Frame(Authentication_displayer)
        authentication_operations_frame.pack(anchor="center", pady=30)
        number_of_authentication_file = len(os.listdir(
            "Browser automation software stored encrypted files/Encrypted Authentication Details"))
        authentication_file_number_Label_string = "Total Encrypted Authentication details - "+ str(number_of_authentication_file) + "\n "
        total_number_of_authentication_details_Label = Label(authentication_operations_frame, text=authentication_file_number_Label_string, font=("Arial", 15, "bold"))
        total_number_of_authentication_details_Label.pack(anchor=CENTER)
        all_non_altering_items_frame = Frame(authentication_operations_frame)
        all_non_altering_items_frame.pack(anchor="center")
        all_altering_item_frame = Frame(authentication_operations_frame)
        all_altering_item_frame.pack(anchor="center")

        all_detection_item_frame = Frame(authentication_operations_frame)
        all_detection_item_frame.pack(anchor="center")

        # lazy_load_authentication_details_Label = Label(authentication_operations_frame, text="Enter lazy load value:")
        # lazy_load_authentication_details_Label.grid(row=0, column=0)
        decrypting_item_frame = Frame(all_non_altering_items_frame, padx=10)
        decrypting_item_frame.grid(row=0, column=0)
        lazy_load_authentication_details_entry = customtkinter.CTkEntry(decrypting_item_frame, font=("Courier", 15, "bold"), corner_radius=50, width=75, placeholder_text="Index")
        lazy_load_authentication_details_entry.grid(row=0, column=0)
        lazy_load_authentication_details_entry.insert(END, "5")
        lazy_load_authentication_details_button = customtkinter.CTkButton(decrypting_item_frame, text="Decrypt", command=get_lazy_load_from_entry_field_and_decrypt_authentication_Details, font=("Arial", 13, "bold"), width=80)
        lazy_load_authentication_details_button.grid(row=0, column=1)
        # ========================================================== #
        deleting_item_frame = Frame(all_non_altering_items_frame)
        deleting_item_frame.grid(row=0, column=1, padx=10)
        # delete_authentication_details_Label = Label(deleting_item_frame, text="Enter index value to delete :")
        # delete_authentication_details_Label.grid(row=1, column=0)
        delete_authentication_details_entry = customtkinter.CTkEntry(deleting_item_frame, font=("Courier", 15, "bold"), corner_radius=50, width=75, placeholder_text="Index")
        delete_authentication_details_entry.grid(row=0, column=0)
        delete_authentication_details_button = customtkinter.CTkButton(deleting_item_frame, text="Delete", command=get_index_value_from_entry_field_and_delete_the_authentication_details, font=("Arial", 13, "bold"), width=80)
        delete_authentication_details_button.grid(row=0, column=1)
        altering_item_frame = Frame(all_altering_item_frame)
        altering_item_frame.grid(row=1, column=0, pady=10)
        index_entry_field_of_authentication_Details = customtkinter.CTkEntry(altering_item_frame, font=("Courier", 15, "bold"), corner_radius=50, width=75, placeholder_text="Index")
        index_entry_field_of_authentication_Details.grid(row=0, column=0, padx=5)
        website_entry_field_of_authentication_details = customtkinter.CTkEntry(altering_item_frame, font=("Courier", 15, "bold"), corner_radius=50, width=100, placeholder_text="Website")
        website_entry_field_of_authentication_details.grid(row=0, column=1, padx=5)
        username_entry_field_of_authentication_details = customtkinter.CTkEntry(altering_item_frame, font=("Courier", 15, "bold"), corner_radius=50, width=100, placeholder_text="Username")
        username_entry_field_of_authentication_details.grid(row=0, column=2, padx=5)
        password_entry_field_of_authentication_details = customtkinter.CTkEntry(altering_item_frame,
                                                                                font=("Courier", 15, "bold"),
                                                                                corner_radius=50, width=100,
                                                                                placeholder_text="Password")
        password_entry_field_of_authentication_details.grid(row=0, column=3, padx=5)
        add_authentication_details_button = customtkinter.CTkButton(altering_item_frame, text="Add",
                                                                       font=("Arial", 13, "bold"), width=50, command=add_authentication_from_entries)
        add_authentication_details_button.grid(row=0, column=4, padx=5)
        edit_authentication_details_button = customtkinter.CTkButton(altering_item_frame, text="Edit",
                                                                    font=("Arial", 13, "bold"), width=50, command=edit_authentication_details_from_entries)
        edit_authentication_details_button.grid(row=0, column=5)
        # ============================================================ #
        use_authentications_Frame = Frame(all_non_altering_items_frame)
        use_authentications_Frame.grid(row=0, column=2, padx=15)
        # use_authentication_details_Label = Label(use_authentications_Frame, text="Enter the index to use:")
        # use_authentication_details_Label.grid(row=4, column=0)
        use_authentication_details_entry = customtkinter.CTkEntry(use_authentications_Frame, font=("Courier", 15, "bold"), corner_radius=50, width=75, placeholder_text="Index")
        use_authentication_details_entry.grid(row=0, column=0)
        username_authentication_details_button = customtkinter.CTkButton(use_authentications_Frame, text="username", command=get_username_from_index, font=("Arial", 13, "bold"), width=80)
        username_authentication_details_button.grid(row=0, column=1, padx=4)
        password_authentication_details_button = customtkinter.CTkButton(use_authentications_Frame, text="password", command=get_password_from_index, font=("Arial", 13, "bold"), width=80)
        password_authentication_details_button.grid(row=0, column=2)
        website_button = customtkinter.CTkButton(use_authentications_Frame, text="Website",
                                                                         command=get_website_from_index,
                                                                         font=("Arial", 13, "bold"), width=80)
        website_button.grid(row=0, column=3, padx=4)
        automatic_u_p_switch_button = customtkinter.CTkButton(use_authentications_Frame, text="Automatic",
                                                 command=automatic_switch,
                                                 font=("Arial", 13, "bold"), width=80)
        automatic_u_p_switch_button.grid(row=0, column=4)

        detection_click_button = customtkinter.CTkButton(use_authentications_Frame, text="Activate Detection",
                                                              command=activate_detection__image_auth__,
                                                              font=("Arial", 13, "bold"), width=80)
        detection_click_button.grid(row=0, column=5, padx=4)


        index_of_the_detection___which_one = customtkinter.CTkEntry(all_detection_item_frame, font=("Courier", 15, "bold"), corner_radius=50, width=75, placeholder_text="Index")
        index_of_the_detection___which_one.grid(row=0, column=0)

        detection_modification_button = customtkinter.CTkButton(all_detection_item_frame, text="Modify Detection", command=pop_up_authentication_detection_modification_window,
                                                 font=("Arial", 13, "bold"), width=80)
        detection_modification_button.grid(row=0, column=1)

        # ============================================================ #
        scroll_bar_for_authentication_tree_view = Scrollbar(Authentication_displayer)
        scroll_bar_for_authentication_tree_view.pack(side=RIGHT, fill=Y)
        authentication_tree_view = ttk.Treeview(Authentication_displayer, selectmode="browse")
        authentication_tree_view.pack(anchor="center")
        authentication_tree_view.configure(yscrollcommand=scroll_bar_for_authentication_tree_view.set)
        authentication_tree_view["columns"] = ("1", "2", "3", "4")
        authentication_tree_view["show"] = "headings"
        authentication_tree_view.column("1", width=100, anchor="c")
        authentication_tree_view.column("2", width=300, anchor="c")
        authentication_tree_view.column("3", width=400, anchor="c")
        authentication_tree_view.column("4", width=400,anchor="c")
        authentication_tree_view.heading("1", text="Index")
        authentication_tree_view.heading("2", text="Website")
        authentication_tree_view.heading("3", text="Username")
        authentication_tree_view.heading("4", text="Password")
        authentication_folder_list_of_all_files = os.listdir(
            "Browser automation software stored encrypted files/Encrypted Authentication Details")
        lazy_load_remember_value = 0
        decrypt_and_show_the_authentication_details_with_lazy_load_values(lazy_load_value=5)
        scroll_bar_for_authentication_tree_view.config(command=authentication_tree_view.yview)


def activate_detection__image_auth__():
    global detection__image_auth__LOCK___
    detection__image_auth__LOCK___ = 0
    get_modification_image_detection_list()
    print("Successfully activated the image detection")

def deactivate_detection__image_auth__():
    global detection__image_auth__LOCK___
    detection__image_auth__LOCK___ = 1
    print("Successfully Deactivated the image detection")

def get_modification_image_detection_list():
    global authentication_folder_list_of_all_files, use_authentication_details_entry, __loaded_all_prev_3_confidence_levels_details__, __loaded_all_website_image_details__, __loaded_all_username_image_details__, __loaded_all_password_image_details__
    __not_proper__file_name___ = authentication_folder_list_of_all_files[int(use_authentication_details_entry.get())]
    proper_file_name = __not_proper__file_name___[0:-4] + " ( B A S ) ( Image detection data ).pkl"
    the_main_loading_file = "Browser automation important cache files/modification image detection list details/"+proper_file_name
    image_detection_details___File___existence = os.path.exists(the_main_loading_file)
    if image_detection_details___File___existence is False:
        print("Error: Detection file doesn't exists")
    else:
        with open(the_main_loading_file, "rb") as image_detection_details_file:
            image_details = pickle.load(image_detection_details_file)
            __loaded_all_prev_3_confidence_levels_details__ = list(image_details["all_3_confidence_levels"])
            __loaded_all_website_image_details__ = list(image_details["website image paths"])
            __loaded_all_username_image_details__ = list(image_details["username image paths"])
            __loaded_all_password_image_details__ = list(image_details["password image paths"])


def detect_and_click_on_username_image_and_enter_username_name():
    global __loaded_all_prev_3_confidence_levels_details__, __loaded_all_website_image_details__, __loaded_all_username_image_details__, __loaded_all_password_image_details__, lock_all_function, detection__image_auth__LOCK___
    if detection__image_auth__LOCK___ == 0:
        get_username_from_index()
        click_on_detected_modification_image(details_list=__loaded_all_username_image_details__, ___w_u_p__select__=1)
    else:
        print("Alert: Detection not activated.")
    # List of image paths

def detect_and_click_on_password_image_and_enter_password_name():
    global __loaded_all_prev_3_confidence_levels_details__, __loaded_all_website_image_details__, __loaded_all_username_image_details__, __loaded_all_password_image_details__, lock_all_function, detection__image_auth__LOCK___
    if detection__image_auth__LOCK___ == 0:
        get_password_from_index()
        click_on_detected_modification_image(details_list=__loaded_all_password_image_details__, ___w_u_p__select__=2)
    else:
        print("Alert: Detection not activated.")


def detect_and_click_on_website_image_and_enter_website_name():
    global __loaded_all_prev_3_confidence_levels_details__, __loaded_all_website_image_details__, __loaded_all_username_image_details__, __loaded_all_password_image_details__, lock_all_function, detection__image_auth__LOCK___
    if detection__image_auth__LOCK___ == 0:
        get_website_from_index()
        click_on_detected_modification_image(details_list=__loaded_all_website_image_details__, ___w_u_p__select__=0)
    else:
        print("Alert: Detection not activated.")

def click_on_detected_modification_image(details_list, ___w_u_p__select__):
    global __loaded_all_prev_3_confidence_levels_details__
    image_paths = details_list

    # Flag to track if any image is found
    image_found = False

    # Loop through the list of image paths
    for path in range(len(image_paths)):
        confidence_level = float(__loaded_all_prev_3_confidence_levels_details__[path][int(___w_u_p__select__)])
        image_location = pyautogui.locateOnScreen(image_paths[path], confidence=confidence_level)
        print(confidence_level)
        if image_location is not None:
            # Image found
            # print("Image found at:", image_location)
            image_found = True
            pyautogui.moveTo(image_location)
            pyautogui.doubleClick()
            pyautogui.keyDown("ctrl")
            pyautogui.press("v")
            pyautogui.keyUp("ctrl")
            break  # Exit the loop once a match is found

    if not image_found:
        print("None of the images found")


def read_the_ath_details_image_detection_file():
    global index_of_the_detection___which_one, authentication_folder_list_of_all_files, modification_image_detection_file_name
    detection_file_name = authentication_folder_list_of_all_files[int(index_of_the_detection___which_one.get())]
    refactored_detection_File_name = detection_file_name[0:-4] + " ( B A S ) ( Image detection data ).pkl"
    modification_image_detection_file_name = "Browser automation important cache files/modification image detection list details/"+refactored_detection_File_name
    image_detection_details___File___existence = os.path.exists(modification_image_detection_file_name)
    if image_detection_details___File___existence is False:
        print("Creating a image detection file ...")
        image_detection_file_content = {
            "all_3_confidence_levels": [],
            "website image paths": [],
            "username image paths": [],
            "password image paths": []
        }
        with open(modification_image_detection_file_name, "wb") as image_detection_file:
            pickle.dump(image_detection_file_content, image_detection_file)
            print("Successfully created an image detection file.")


def add_image_detection_details():
    global website_confidence_entry_field_of_authentication_image_detection, username_confidence_entry_field_of_authentication_image_detection, password_confidence_entry_field_of_authentication_image_detection, website_entry_field_of_authentication_image_detection, username_entry_field_of_authentication_image_detection, password_entry_field_of_authentication_image_detection, modification_image_detection_file_name
    website_confidence_level = str(website_confidence_entry_field_of_authentication_image_detection.get()) + " "
    username_confidence_level = str(username_confidence_entry_field_of_authentication_image_detection.get() )+ " "
    password_confidence_level = str(password_confidence_entry_field_of_authentication_image_detection.get()) + " "
    website_image_path = str(website_entry_field_of_authentication_image_detection.get()) + " "
    username_image_path = str(username_entry_field_of_authentication_image_detection.get()) + " "
    password_image_path = str(password_entry_field_of_authentication_image_detection.get()) + " "
    if website_confidence_level.isspace() is True:
        website_confidence_level = "1"
    if username_confidence_level.isspace() is True:
        username_confidence_level = "1"
    if password_confidence_level.isspace() is True:
        password_confidence_level = "1"
    if not website_image_path.isspace() and not username_image_path.isspace() and not password_image_path.isspace():
        nested_confidence_level_list = [float(website_confidence_level), float(username_confidence_level), float(password_confidence_level)]
        with open(modification_image_detection_file_name, "rb") as previous_image_details_file:
            prev_details = pickle.load(previous_image_details_file)
            all_prev_3_confidence_levels = list(prev_details["all_3_confidence_levels"])
            all_website_image_paths = list(prev_details["website image paths"])
            all_username_image_paths = list(prev_details["username image paths"])
            all_password_image_paths = list(prev_details["password image paths"])
            all_prev_3_confidence_levels.append(nested_confidence_level_list)
            all_website_image_paths.append(website_image_path[0:-1])
            all_username_image_paths.append(username_image_path[0:-1])
            all_password_image_paths.append(password_image_path[0:-1])
            # print(type(all_prev_3_confidence_levels), type(all_website_image_paths), type(all_username_image_paths), type(all_password_image_paths))
            image_detection_file_content = {
                "all_3_confidence_levels": all_prev_3_confidence_levels,
                "website image paths": all_website_image_paths,
                "username image paths": all_username_image_paths,
                "password image paths":all_password_image_paths
            }

        with open(modification_image_detection_file_name, "wb") as refactoring_file:
            pickle.dump(image_detection_file_content, refactoring_file)
            print("Successfully added")
        display_all_modification_image_detection_details()
    else:
        website_entry_field_of_authentication_image_detection.delete(0, END)
        username_entry_field_of_authentication_image_detection.delete(0, END)
        password_entry_field_of_authentication_image_detection.delete(0, END)
        print("Error: Not filled the entries properly")


def delete_image_detection_details():
    global modification_image_detection_file_name, index_entry_field_of_authentication_image_detection
    index_for_deletion = int(index_entry_field_of_authentication_image_detection.get())
    with open(modification_image_detection_file_name, "rb") as deleting_data:
        loaded_data = pickle.load(deleting_data)
        all_prev_3_confidence_levels = list(loaded_data["all_3_confidence_levels"])
        all_website_image_paths = list(loaded_data["website image paths"])
        all_username_image_paths = list(loaded_data["username image paths"])
        all_password_image_paths = list(loaded_data["password image paths"])
    all_prev_3_confidence_levels.pop(index_for_deletion)
    all_website_image_paths.pop(index_for_deletion)
    all_username_image_paths.pop(index_for_deletion)
    all_password_image_paths.pop(index_for_deletion)
    image_detection_file_content = {
        "all_3_confidence_levels": all_prev_3_confidence_levels,
        "website image paths": all_website_image_paths,
        "username image paths": all_username_image_paths,
        "password image paths": all_password_image_paths
    }
    with open(modification_image_detection_file_name, "wb") as refactoring_file:
        pickle.dump(image_detection_file_content, refactoring_file)
        print("Successfully Deleted")
    display_all_modification_image_detection_details()

    # print(all_prev_3_confidence_levels, all_website_image_paths, all_username_image_paths, all_password_image_paths)

def editing_image_detection_details():
    global index_entry_field_of_authentication_image_detection, website_confidence_entry_field_of_authentication_image_detection, username_confidence_entry_field_of_authentication_image_detection, password_confidence_entry_field_of_authentication_image_detection, website_entry_field_of_authentication_image_detection, username_entry_field_of_authentication_image_detection, password_entry_field_of_authentication_image_detection, modification_image_detection_file_name
    index_for_editing = str(index_entry_field_of_authentication_image_detection.get())
    website_confidence_level = str(website_confidence_entry_field_of_authentication_image_detection.get()) + " "
    username_confidence_level = str(username_confidence_entry_field_of_authentication_image_detection.get()) + " "
    password_confidence_level = str(password_confidence_entry_field_of_authentication_image_detection.get()) + " "
    website_image_path = str(website_entry_field_of_authentication_image_detection.get()) + " "
    username_image_path = str(username_entry_field_of_authentication_image_detection.get()) + " "
    password_image_path = str(password_entry_field_of_authentication_image_detection.get()) + " "
    if index_for_editing.isnumeric() is True:
        with open(modification_image_detection_file_name, "rb") as deleting_data:
            loaded_data = pickle.load(deleting_data)
            all_3_confidence_levels = list(loaded_data["all_3_confidence_levels"])
            all_website_image_paths = list(loaded_data["website image paths"])
            all_username_image_paths = list(loaded_data["username image paths"])
            all_password_image_paths = list(loaded_data["password image paths"])
        if website_confidence_level.isspace():
            website_confidence_level = float(all_3_confidence_levels[int(index_for_editing)][0])
        if username_confidence_level.isspace():
            username_confidence_level = float(all_3_confidence_levels[int(index_for_editing)][1])
        if password_confidence_level.isspace():
            password_confidence_level = float(all_3_confidence_levels[int(index_for_editing)][2])
        if website_image_path.isspace():
            website_image_path = str(all_website_image_paths[int(index_for_editing)]) + " "
        if username_image_path.isspace():
            username_image_path = str(all_username_image_paths[int(index_for_editing)]) + " "
        if password_image_path.isspace():
            password_image_path = str(all_password_image_paths[int(index_for_editing)]) + " "

        nested_confidence_list = [float(website_confidence_level), float(username_confidence_level), float(password_confidence_level)]
        all_3_confidence_levels.insert(int(index_for_editing), nested_confidence_list)
        all_website_image_paths.insert(int(index_for_editing), website_image_path[0:-1])
        all_username_image_paths.insert(int(index_for_editing), username_image_path[0:-1])
        all_password_image_paths.insert(int(index_for_editing), password_image_path[0:-1])

        all_3_confidence_levels.pop((int(index_for_editing)+1))
        all_website_image_paths.pop((int(index_for_editing)+1))
        all_username_image_paths.pop((int(index_for_editing)+1))
        all_password_image_paths.pop((int(index_for_editing)+1))

        image_detection_file_content = {
            "all_3_confidence_levels": all_3_confidence_levels,
            "website image paths": all_website_image_paths,
            "username image paths": all_username_image_paths,
            "password image paths": all_password_image_paths
        }
        with open(modification_image_detection_file_name, "wb") as refactoring_file:
            pickle.dump(image_detection_file_content, refactoring_file)
            print("Successfully Edited")
        display_all_modification_image_detection_details()
    else:
        print("Error: Not filled the entries properly")


def display_all_modification_image_detection_details():
    global modification_image_detection_file_name, authentication_detection_paths_of____images____tree_view, authentication_total_images_for_detection_label
    try:
        authentication_detection_paths_of____images____tree_view.delete(*authentication_detection_paths_of____images____tree_view.get_children())
    except:
        pass
    with open(modification_image_detection_file_name, "rb") as loaded_file:
        all_details_of_all_types = pickle.load(loaded_file)
        ___prev_3_confidence_levels = list(all_details_of_all_types["all_3_confidence_levels"])
        ___website_image_paths = list(all_details_of_all_types["website image paths"])
        ___username_image_paths = list(all_details_of_all_types["username image paths"])
        ___password_image_paths = list(all_details_of_all_types["password image paths"])
    authentication_total_images_for_detection_label.configure(text="Total detection images - "+str(len(___prev_3_confidence_levels)))
    for i in range(len(___prev_3_confidence_levels)):
        authentication_detection_paths_of____images____tree_view.insert("", "end",
                                        values=(i, ___prev_3_confidence_levels[i][0], ___website_image_paths[i], ___prev_3_confidence_levels[i][1], ___username_image_paths[i], ___prev_3_confidence_levels[i][2], ___password_image_paths[i]))


def pop_up_authentication_detection_modification_window():
    global Authentication_displayer, index_of_the_detection___which_one, authentication_folder_list_of_all_files, index_entry_field_of_authentication_image_detection, website_confidence_entry_field_of_authentication_image_detection, username_confidence_entry_field_of_authentication_image_detection, password_confidence_entry_field_of_authentication_image_detection, website_entry_field_of_authentication_image_detection, username_entry_field_of_authentication_image_detection, password_entry_field_of_authentication_image_detection, authentication_detection_paths_of____images____tree_view, authentication_total_images_for_detection_label
    read_the_ath_details_image_detection_file()
    Main_ath_detection_window = Toplevel(Authentication_displayer)
    Main_ath_detection_window.title("Authentication detection modification window")
    authentication_total_images_for_detection_label =  Label(Main_ath_detection_window, text="Total detection images - Error", font=("Arial", 15, "bold"))
    authentication_total_images_for_detection_label.pack(anchor=CENTER, pady=10)
    all_Altering_widget_frame = Frame(Main_ath_detection_window)
    all_Altering_widget_frame.pack(anchor=CENTER, pady=10)

    index_entry_field_of_authentication_image_detection = customtkinter.CTkEntry(all_Altering_widget_frame,
                                                                         font=("Courier", 15, "bold"), corner_radius=50,
                                                                         width=75, placeholder_text="Index")
    index_entry_field_of_authentication_image_detection.grid(row=0, column=0, padx=5)

    website_confidence_entry_field_of_authentication_image_detection = customtkinter.CTkEntry(all_Altering_widget_frame,
                                                                                   font=("Courier", 15, "bold"),
                                                                                   corner_radius=50, width=100,
                                                                                   placeholder_text="web cnfdc")  #  website image confidence number
    website_confidence_entry_field_of_authentication_image_detection.grid(row=0, column=1, padx=5)

    username_confidence_entry_field_of_authentication_image_detection = customtkinter.CTkEntry(all_Altering_widget_frame,
                                                                                      font=("Courier", 15, "bold"),
                                                                                      corner_radius=50, width=100,
                                                                                      placeholder_text="U.N cnfdc")  #  username image confidence number
    username_confidence_entry_field_of_authentication_image_detection.grid(row=0, column=2, padx=5)

    password_confidence_entry_field_of_authentication_image_detection = customtkinter.CTkEntry(all_Altering_widget_frame,
                                                                                      font=("Courier", 15, "bold"),
                                                                                      corner_radius=50, width=100,
                                                                                      placeholder_text="P. cnfdc")  #  password image confidence number
    password_confidence_entry_field_of_authentication_image_detection.grid(row=0, column=3, padx=5)


    website_entry_field_of_authentication_image_detection = customtkinter.CTkEntry(all_Altering_widget_frame,
                                                                           font=("Courier", 15, "bold"),
                                                                           corner_radius=50, width=100,
                                                                           placeholder_text="Website")  #  path of website image
    website_entry_field_of_authentication_image_detection.grid(row=0, column=4, padx=5)
    username_entry_field_of_authentication_image_detection = customtkinter.CTkEntry(all_Altering_widget_frame,
                                                                            font=("Courier", 15, "bold"),
                                                                            corner_radius=50, width=100,
                                                                            placeholder_text="Username")  #  path of username image
    username_entry_field_of_authentication_image_detection.grid(row=0, column=5, padx=5)
    password_entry_field_of_authentication_image_detection = customtkinter.CTkEntry(all_Altering_widget_frame,
                                                                            font=("Courier", 15, "bold"),
                                                                            corner_radius=50, width=100,
                                                                            placeholder_text="Password")  #  path of password image
    password_entry_field_of_authentication_image_detection.grid(row=0, column=6, padx=5)
    add_authentication_image_detection_button = customtkinter.CTkButton(all_Altering_widget_frame, text="Add",
                                                                font=("Arial", 13, "bold"), width=50,
                                                                command=add_image_detection_details)
    add_authentication_image_detection_button.grid(row=0, column=7, padx=5)
    edit_authentication_details_button = customtkinter.CTkButton(all_Altering_widget_frame, text="Edit",
                                                                 font=("Arial", 13, "bold"), width=50,
                                                                 command=editing_image_detection_details)
    edit_authentication_details_button.grid(row=0, column=8)

    delete_button_for_detection_modification = customtkinter.CTkButton(all_Altering_widget_frame, text="DELETE",
                                                              font=("Arial", 13, "bold"), corner_radius=10,
                                                              width=5, fg_color="red", hover_color="red3", command=delete_image_detection_details)
    delete_button_for_detection_modification.grid(row=0, column=9, padx=5)


    tree_view_frame = Frame(Main_ath_detection_window)
    tree_view_frame.pack(anchor=CENTER)

    scroll_bar_for_authentication____detection____tree_view = Scrollbar(tree_view_frame)
    scroll_bar_for_authentication____detection____tree_view.pack(side=RIGHT, fill=Y)
    authentication_detection_paths_of____images____tree_view = ttk.Treeview(tree_view_frame, selectmode="browse")
    authentication_detection_paths_of____images____tree_view.pack(anchor="center")
    authentication_detection_paths_of____images____tree_view.configure(yscrollcommand=scroll_bar_for_authentication____detection____tree_view.set)
    authentication_detection_paths_of____images____tree_view["columns"] = ("1", "2", "3", "4", "5", "6", "7")
    authentication_detection_paths_of____images____tree_view["show"] = "headings"
    authentication_detection_paths_of____images____tree_view.column("1", width=100, anchor="c")

    authentication_detection_paths_of____images____tree_view.column("2", width=100, anchor="c")

    authentication_detection_paths_of____images____tree_view.column("3", width=450, anchor="c")

    authentication_detection_paths_of____images____tree_view.column("4", width=100, anchor="c")

    authentication_detection_paths_of____images____tree_view.column("5", width=450, anchor="c")
    #
    authentication_detection_paths_of____images____tree_view.column("6", width=100, anchor="c")

    authentication_detection_paths_of____images____tree_view.column("7", width=450, anchor="c")
    authentication_detection_paths_of____images____tree_view.heading("1", text="Index")

    authentication_detection_paths_of____images____tree_view.heading("2", text="web confi")

    authentication_detection_paths_of____images____tree_view.heading("3", text="Website's image paths")

    authentication_detection_paths_of____images____tree_view.heading("4", text="U.N confi")

    authentication_detection_paths_of____images____tree_view.heading("5", text="Username's image paths")

    authentication_detection_paths_of____images____tree_view.heading("6", text="P. confi")

    authentication_detection_paths_of____images____tree_view.heading("7", text="Password's image paths")

    scroll_bar_for_authentication____detection____tree_view.config(command=authentication_detection_paths_of____images____tree_view.yview)
    display_all_modification_image_detection_details()



def authentication_decrypter(value):
    global matching_key_hashed
    try:
        key = key_derive()
        if double_encryption_key_generator(value=(key.decode())) == matching_key_hashed:
            decryption_key = key
            decrypter = Fernet(decryption_key)
            decrypted_value = decrypter.decrypt(value)
            return decrypted_value.decode()
    except:
        print("Error: some error while decrypting")


def decrypt_and_show_the_authentication_details_with_lazy_load_values(lazy_load_value):
    global authentication_folder_list_of_all_files, authentication_tree_view, lazy_load_remember_value
    try:
        for i in range(lazy_load_value):
            auth_file_name = authentication_folder_list_of_all_files[i+lazy_load_remember_value]
            with open(("Browser automation software stored encrypted files/Encrypted Authentication Details/" + auth_file_name), "rb") as fn:
                auth_file = pickle.load(fn)
            auth_head = auth_file["website"]
            auth_username = authentication_decrypter(value=auth_file["username"])
            auth_password = authentication_decrypter(value=auth_file["password"])
            authentication_tree_view.insert("", "end", values=((i+lazy_load_remember_value), auth_head, auth_username, auth_password))
        lazy_load_remember_value += lazy_load_value
        # print(lazy_load_remember_value)
    except:
        lazy_load_remember_value = len(authentication_folder_list_of_all_files)


def get_index_clipboard():
    global values_in_list, index_of_clipboards_entry
    index_value_clipb = index_of_clipboards_entry.get()
    if index_value_clipb.isnumeric() is True:
        try:
            pyperclip.copy(values_in_list[int(index_value_clipb)])
        except:
            print("Error: index value may be out of range")


def pop_up_decrypt_and_show_clipboards():
    global decrypt_and_show_window, decrypt_and_show_list, index_of_clipboards_entry, value_of_lazy_loading_clipboards_entry, total_lines, range_of_clipboards_to_delete_entry
    if double_encryption_key_generator(value=key_derive().decode()) == matching_key_hashed:
        try:
            with open(
                    "Browser automation software stored encrypted files//encrypted clipboards//encrypted clipboards.enc",
                      "rb") as enc_file_:
                total_lines = enc_file_.readlines()
                total_lines = len(total_lines)
            decrypt_and_show_window = Toplevel(Input_Window)
            decrypt_and_show_window.title("Decrypted clipboard items")
            decrypt_and_show_window.minsize(width=950, height=410)
            decrypt_and_show_window.maxsize(width=950, height=410)
            total_clipboards_label = Label(decrypt_and_show_window,
                                           text=("Total encrypted clipboards -  " + str(total_lines)), font=("Arial", 15, "bold"))
            total_clipboards_label.pack(anchor="center", pady=10)
            index_get_frame = Frame(decrypt_and_show_window, pady=20)
            index_get_frame.pack(anchor=CENTER)
            decrypt_frame = Frame(index_get_frame)
            decrypt_frame.grid(row=0, column=0, padx=40, pady=10)
            copy_clipboard_frame = Frame(index_get_frame)
            copy_clipboard_frame.grid(row=0, column=1, padx=40, pady=10)
            delete_clipboard_frame = Frame(index_get_frame)
            delete_clipboard_frame.grid(row=0, column=2, padx=40, pady=10)
            more_info_label(tooltip_Text="Enter the Lazy-load value", abscissa=240,
                            ordinate=14, window=index_get_frame, Wrap_l=150, side="right", side_left_distance_y=0, side_left_distance_x=0)
            more_info_label(tooltip_Text="Enter the index to copy clipboard", abscissa=565,
                            ordinate=14, window=index_get_frame, Wrap_l=150, side="right", side_left_distance_y=0, side_left_distance_x=0)
            more_info_label(tooltip_Text="Enter the range in the form Lower limit index-Upper limit index, clipboards including these limits and clipboards between them will be deleted", abscissa=840,
                            ordinate=14, window=index_get_frame, Wrap_l=300, side="left", side_left_distance_x=330, side_left_distance_y=30)
            # decrypting_value_skips_clipboards_Label = Label(index_get_frame, text="Value for lazy loading - ", font=("Arial", 10, "bold", "italic"))
            # decrypting_value_skips_clipboards_Label.grid(row=1, column=0)
            value_of_lazy_loading_clipboards_entry = customtkinter.CTkEntry(decrypt_frame, font=("Courier", 15, "bold"), corner_radius=50, width=75)
            value_of_lazy_loading_clipboards_entry.grid(row=0, column=0)
            value_of_lazy_loading_clipboards_entry.insert(0, 9)
            get_index_value_lazy_loading_clipboard = customtkinter.CTkButton(decrypt_frame, text='Decrypt', font=("Arial", 13, "bold"), command=decrypt_only_limit_iteration_clipboard, width=80)
            get_index_value_lazy_loading_clipboard.grid(row=0, column=1)

            index_of_clipboards_entry = customtkinter.CTkEntry(copy_clipboard_frame, font=("Courier", 15, "bold"), corner_radius=50, width=75)
            index_of_clipboards_entry.grid(row=0, column=2)
            get_index_value = customtkinter.CTkButton(copy_clipboard_frame, text="Copy Clipboard", font=("Arial", 13, "bold"),
                                     command=get_index_clipboard, width=120)
            get_index_value.grid(row=0, column=3)

            range_of_clipboards_to_delete_entry = customtkinter.CTkEntry(delete_clipboard_frame, font=("Courier", 15, "bold"), corner_radius=50, width=75)
            range_of_clipboards_to_delete_entry.grid(row=0, column=4)
            get_range_value_for_deletion = customtkinter.CTkButton(delete_clipboard_frame, text="Delete", font=("Arial", 13, "bold"),
                                     command=get_values_from_entry_fields_for_deletion, width=80)
            get_range_value_for_deletion.grid(row=0, column=5)

            scroll_bar = Scrollbar(decrypt_and_show_window)
            scroll_bar.pack(side=RIGHT, fill=Y)
            decrypt_and_show_list = Listbox(decrypt_and_show_window, yscrollcommand=scroll_bar.set, width=90, height=10, font=("Arial", 10), borderwidth=2)
            scroll_bar.config(command=decrypt_and_show_list.yview)
            decrypt_and_show_list.pack(padx=30)
            clipboard_read_file_line_by_line()
        except:
            print("Error: Invalid password")


def create_blank_folder_files():
    global create_a_folder_file_entry_field, take_notes_to_be_displayed_window
    folder_name = str(create_a_folder_file_entry_field.get())
    blank_folder_file_data = {
        "paths":[]
    }
    if folder_name != "":
        if folder_name.isspace() is False:
            with open("Folder Holding Files/"+folder_name+"( B A S ).pkl", "wb") as folder_file:
                pickle.dump(blank_folder_file_data, folder_file)
            take_notes_to_be_displayed_window.destroy()
            pop_up_folder_files_window()


def delete_folder_files():
    global index_of_folder_to_delete_entry, folder_files_paths, take_notes_to_be_displayed_window
    the_folder_deletion_index = str(index_of_folder_to_delete_entry.get())
    if the_folder_deletion_index.isnumeric() is True:
        if folder_files_paths[int(the_folder_deletion_index)] != "General( B A S ).pkl":
            os.remove("Folder Holding Files/"+str(folder_files_paths[int(the_folder_deletion_index)]))
            take_notes_to_be_displayed_window.destroy()
            pop_up_folder_files_window()
        else:
            print("Error: You can't delete General folder.")


def process_index_and_get_paths_in_a_list(index_string):
    global folder_index_entry_field, image_index_for_folder_entry_field, screenshots_paths, index_to_paths
    string_of_indexes = index_string+","
    previous_index = 0
    index_to_paths = []
    pre_init_paths = []
    for comma_separate in range(len(string_of_indexes)):
        if string_of_indexes[comma_separate] == ",":
            the_index_for_exclusion = string_of_indexes[previous_index:comma_separate]
            previous_index = comma_separate + 1
            try:
                paths_name_from_index = screenshots_paths[(int(the_index_for_exclusion) - 1)]
                pre_init_paths.append(str(paths_name_from_index))
            except:
                folder_index_entry_field.delete(0, "end")
                image_index_for_folder_entry_field.delete(0, "end")
    for item in pre_init_paths:
        if item not in index_to_paths:
            index_to_paths.append(item)
    return index_to_paths


def get_folder_index_and_image_index_and_process_it():
    global folder_index_entry_field, image_index_for_folder_entry_field, index_value_init
    folder_index_for_Adding = str(folder_index_entry_field.get())
    image_index_for_adding_to_folder = str(image_index_for_folder_entry_field.get())
    if image_index_for_adding_to_folder == "":
        image_index_for_adding_to_folder = str(index_value_init+1)
    if folder_index_for_Adding.isnumeric() is True:
        p = os.listdir("Folder Holding Files")
        if p[int(folder_index_for_Adding)] != "General( B A S ).pkl":
            entered_paths_list = process_index_and_get_paths_in_a_list(index_string=image_index_for_adding_to_folder)
            with open("Folder Holding Files/"+str(p[int(folder_index_for_Adding)]), "rb") as manipulation_folder_file:
                prev_data = pickle.load(manipulation_folder_file)
                prev_list_of_paths = prev_data["paths"]
            for ot in range(len(prev_list_of_paths)):
                item_hash = prev_list_of_paths[ot]
                entered_paths_list.append(item_hash)
            entered_paths_list = list(set(entered_paths_list))

            folder_file_data = {
                "paths": entered_paths_list
            }
            with open("Folder Holding Files/"+str(p[int(folder_index_for_Adding)]), "wb") as reassign_folder_file:
                pickle.dump(folder_file_data, reassign_folder_file)
                print("Successfully Added the provided images")
        else:
            print("Error: You can't add anything to this folder")


def insert_folder_name_with_index():
    global show_folder_list, folder_files_paths
    for index in range(len(folder_files_paths)):
        with open("Folder Holding Files/"+folder_files_paths[index], "rb") as list_len_calculate:
            if folder_files_paths[index] != "General( B A S ).pkl":
                length_file = pickle.load(list_len_calculate)
                getting_data = length_file["paths"]
                length = len(getting_data)
            else:
                length = len(os.listdir("Browser automation software stored encrypted files/Encrypted screenshots"))
        folder_name_with_index = str(index) + " " + (str(folder_files_paths[index]))[0:-13] + "; Total Images present - " + str(length)
        show_folder_list.insert(END, folder_name_with_index)


def open_the_folder_and_refactor_paths():
    global index_of_folder_to_open_entry, folder_files_paths, refactored_paths, main_frame_in_video_player, folder_file_name
    folder_index = str(index_of_folder_to_open_entry.get())
    if folder_index.isnumeric() is True:
        if folder_files_paths[int(folder_index)] != "General( B A S ).pkl":
            with open("Folder Holding Files/"+folder_files_paths[int(folder_index)], "rb") as retreive_folder_file:
                folder_file_screenshot_paths = pickle.load(retreive_folder_file)
                refactored_paths = folder_file_screenshot_paths["paths"]
                folder_file_name = str(folder_files_paths[int(folder_index)])
                # print(refactored_paths)
        else:
            General_paths = os.listdir("Browser automation software stored encrypted files/Encrypted screenshots")
            refactored_paths = General_paths
            folder_file_name = "General( B A S ).pkl"
    main_frame_in_video_player.destroy()
    pop_up_decrypt_encrypted_screenshot_image_window()



def pop_up_folder_files_window():
    global main_frame_in_video_player
    global create_a_folder_file_entry_field, index_of_folder_to_delete_entry, folder_files_paths, show_folder_list, take_notes_to_be_displayed_window, index_of_folder_to_open_entry
    if double_encryption_key_generator(value=key_derive().decode()) == matching_key_hashed:
        try:
            folder_files_paths = os.listdir("Folder Holding Files")
            take_notes_to_be_displayed_window = Toplevel(main_frame_in_video_player)
            take_notes_to_be_displayed_window.title("Image Folders")
            take_notes_to_be_displayed_window.minsize(width=1125, height=410)
            take_notes_to_be_displayed_window.maxsize(width=1125, height=410)
            total_folders_present_label = Label(take_notes_to_be_displayed_window,
                                                text=("Total Folders -  " + str(len(folder_files_paths))), font=("Arial", 15, "bold"))
            total_folders_present_label.pack(anchor="center", pady=10)
            index_get_folder_frame = Frame(take_notes_to_be_displayed_window, pady=20)
            index_get_folder_frame.pack(anchor=CENTER)
            sorter_frame = Frame(take_notes_to_be_displayed_window, pady=5)
            sorter_frame.pack(anchor=CENTER)
            create_folder_frame = Frame(index_get_folder_frame)
            create_folder_frame.grid(row=0, column=0, padx=40, pady=10)
            delete_folder_frame = Frame(index_get_folder_frame)
            delete_folder_frame.grid(row=0, column=1, padx=40, pady=10)

            use_folder_frame = Frame(index_get_folder_frame)
            use_folder_frame.grid(row=0, column=2, padx=40, pady=10)

            create_a_folder_file_entry_field = customtkinter.CTkEntry(create_folder_frame, width=200,
                                                                      font=("Arial", 15, "bold"),
                                                                      corner_radius=50, placeholder_text="Folder Name")
            create_a_folder_file_entry_field.grid(row=0, column=0)
            create_folder_button = customtkinter.CTkButton(create_folder_frame, text="Create Folder",
                                                           corner_radius=10,
                                                           width=80,
                                                           font=("Arial", 13, "bold"), command=create_blank_folder_files)
            create_folder_button.grid(row=0, column=1)
            index_of_folder_to_delete_entry = customtkinter.CTkEntry(delete_folder_frame, font=("Courier", 15, "bold"), corner_radius=50, width=75, placeholder_text="Index")
            index_of_folder_to_delete_entry.grid(row=0, column=0)
            get_folder_index_for_deletion = customtkinter.CTkButton(delete_folder_frame, text="Delete", font=("Arial", 13, "bold"), width=80, command=delete_folder_files)
            get_folder_index_for_deletion.grid(row=0, column=1)

            index_of_folder_to_open_entry = customtkinter.CTkEntry(use_folder_frame, font=("Courier", 15, "bold"),
                                                                     corner_radius=50, width=75,
                                                                     placeholder_text="Index")
            index_of_folder_to_open_entry.grid(row=0, column=0)
            get_folder_index_for_opening = customtkinter.CTkButton(use_folder_frame, text="Open Folder",
                                                                    font=("Arial", 13, "bold"), width=80,
                                                                    command=open_the_folder_and_refactor_paths)
            get_folder_index_for_opening.grid(row=0, column=1)

            train_smart_smart_button = customtkinter.CTkButton(sorter_frame, text="Train Smart-sort",
                                                                    font=("Arial", 13, "bold"), width=80,
                                                                    command=print_dataset)
            train_smart_smart_button.grid(row=1, column=1, padx=40)



            scroll_bar0 = Scrollbar(take_notes_to_be_displayed_window)
            scroll_bar0.pack(side=RIGHT, fill=Y)
            show_folder_list = Listbox(take_notes_to_be_displayed_window, yscrollcommand=scroll_bar0.set, width=90, height=10, font=("Arial", 10), borderwidth=2)
            scroll_bar0.config(command=show_folder_list.yview)
            show_folder_list.pack(padx=30)
            insert_folder_name_with_index()
        except:
            print("Error: Invalid password")


#
def print_dataset():
    print("coming")


def note_total_data_used_the_following_day(internet_used_in_this_session, time_used_in_this_session):
    date = time.localtime().tm_mday
    with open("Browser automation important cache files/Total internet usage today.pkl", "rb") as date_file0:  # total internet used, date
        data_retrieving = pickle.load(date_file0)
        previous_date = data_retrieving["date"]
        previous_internet = data_retrieving["total internet used"]
        previous_time = data_retrieving["total time"]
    total_internet = float(previous_internet) + float(internet_used_in_this_session)
    total_time = float(previous_time)+float(time_used_in_this_session)
    if date == previous_date:
        rewrite_dictionary = {
            "date": int(previous_date),
            "total internet used": total_internet, # internet used
            "total time": total_time,
        }
    else:
        rewrite_dictionary = {
            "date": int(date),
            "total internet used": 0,  # internet used
            "total time": 0,
        }
    with open("Browser automation important cache files/Total internet usage today.pkl",
              "wb") as date_file:  # total internet used, date
        pickle.dump(rewrite_dictionary, date_file)


def note_internet_and_time_and_extend___list____format_____for_graphing(internet_used_in_this_session, time_used_in_this_session, average_internet_usage_rate):
    date = time.localtime().tm_mday
    total_internet = []
    total_time = []
    average_internet_usage_list = []
    with open("Browser automation important cache files/internet and time   graphing list data   .pkl", "rb") as graphing_file:  # total internet used, date
        data_retrieving = pickle.load(graphing_file)
        previous_date = data_retrieving["date"]
        previous_internet = list(data_retrieving["Internet list"])
        previous_time = list(data_retrieving["time list"])
        previous_average_rate = list(data_retrieving["average internet rate"])
    for i in range(len(previous_internet)):
        total_internet.append(previous_internet[i])
        total_time.append(previous_time[i])
        average_internet_usage_list.append(previous_average_rate[i])
    total_internet.append(int(internet_used_in_this_session))
    total_time.append(int(time_used_in_this_session))
    average_internet_usage_list.append(float(average_internet_usage_rate))

    if date == previous_date:
        rewrite_dictionary = {
                "date": int(previous_date),
                "Internet list": total_internet, # internet used
                "time list": total_time,
                "average internet rate": average_internet_usage_list,
            }
    else:
        rewrite_dictionary = {
                "date": int(date),
                "Internet list": [0],  # internet used
                "time list": [0],
                "average internet rate": [0],
            }

    with open("Browser automation important cache files/internet and time   graphing list data   .pkl",
              "wb") as refactored_file:  # total internet used, date
        pickle.dump(rewrite_dictionary, refactored_file)
# note_internet_and_time_and_extend___list____format_____for_graphing(internet_used_in_this_session=-8836, time_used_in_this_session=0, average_internet_usage_rate=0.0)


def refresh______():
    date = time.localtime().tm_mday
    rewrite_dictionary = {
        "date": int(date),
        "Internet list": [0],  # internet used
        "time list": [0],
        "average internet rate": [0],
    }
    with open("Browser automation important cache files/internet and time   graphing list data   .pkl",
              "wb") as refactored_file:  # total internet used, date
        pickle.dump(rewrite_dictionary, refactored_file)

# refresh______()

def health_care_system(time_you_watched_this_day_in_seconds):
    if float(time_you_watched_this_day_in_seconds) >= 7200:
        print("Health alert: You have watched more than 2 hour per day.")
        health_alert_prompt = "Health alert; You have watched more than 2 hour per day."
    else:
        print("Its not yet time. You still have time to use.")
        health_alert_prompt = "Its not yet time. You still have "+str(round(((7200-float(time_you_watched_this_day_in_seconds))/3600), 3))+" hours left."
    return health_alert_prompt

def generate_the_required_graphs_of_day_analysis():
    with open("Browser automation important cache files/internet and time   graphing list data   .pkl", "rb") as graphing_file:  # total internet used, date
        data_retrieving = pickle.load(graphing_file)
        internet_list = list(data_retrieving["Internet list"])
        time_list = list(data_retrieving["time list"])
        average_rate_list = list(data_retrieving["average internet rate"])
    int_List____ = []
    for integers___ in range(len(internet_list)):
        int_List____.append(integers___)
    fig, axs = plt.subplots(2, 2)  # 2 rows of subplots
    plt.subplots_adjust(hspace=0.5, wspace=0.5)
    fig.suptitle("Analyses Graphs")
    axs[0, 0].plot(internet_list)
    axs[0, 0].set_title("Internet Usage Graph")
    axs[0, 0].set_xlabel("Number of times executed")
    axs[0, 0].set_ylabel("Internet Used")

    axs[0, 1].plot(time_list)
    axs[0, 1].set_title("Time Usage Graph")
    axs[0, 1].set_xlabel("Number of times executed")
    axs[0, 1].set_ylabel("Time Used")


    axs[1, 0].plot(average_rate_list)
    axs[1, 0].set_title("Average internet usage Graph")
    axs[1, 0].set_xlabel("Number of times executed")
    axs[1, 0].set_ylabel("Average internet rate")

    plt.show()

def pop_up_total_day_analysis():
    total_day_analysis_window = Toplevel(Input_Window)
    total_day_analysis_window.title("Full day analysis")
    note_total_data_used_the_following_day(internet_used_in_this_session=0, time_used_in_this_session=0)
    with open("Browser automation important cache files/Total internet usage today.pkl", "rb") as today_analysis_file_for_health_care:  # total internet used, date
        data_retrieving_for_health = pickle.load(today_analysis_file_for_health_care)
        health_time = data_retrieving_for_health["total time"]
    health_alert_content = health_care_system(time_you_watched_this_day_in_seconds=health_time)
    health_alert_Label = Label(total_day_analysis_window, text=health_alert_content, font=("Arial", 20), foreground="gray5")
    health_alert_Label.pack(anchor=CENTER, pady=10)
    main_frame = LabelFrame(total_day_analysis_window, text="Day Analysis", font=("Courier", 15, "bold"), padx=10, pady=10)
    main_frame.pack(anchor=CENTER, pady=10)
    total_internet_and_time_analysis = Frame(main_frame)
    total_internet_and_time_analysis.pack(anchor=CENTER)
    current_date__ = str(time.localtime().tm_mday)+"/"+str(time.localtime().tm_mon)+"/"+str(time.localtime().tm_year)
    with open("Browser automation important cache files/Total internet usage today.pkl", "rb") as today_analysis_file:  # total internet used, date
        data_retrieving = pickle.load(today_analysis_file)
        internet = str(data_retrieving["total internet used"]) + " Mb used"
        total_time = str(data_retrieving["total time"]) + " Seconds used" + ", " + str(round((data_retrieving["total time"]/60), 3)) + " minutes used"
    day_label = Label(total_internet_and_time_analysis, text="Date:                                ",
                                 font=("Arial", 20), foreground="gray5")
    day_label.grid(row=0, column=0)
    day_show_values_label = Label(total_internet_and_time_analysis, text=str(current_date__), font=("Arial", 20),
                                             foreground="gray5")
    day_show_values_label.grid(row=0, column=1)
    total_internet_label = Label(total_internet_and_time_analysis, text="Total internet used today: ", font=("Arial", 20), foreground="gray5")
    total_internet_label.grid(row=1, column=0)
    total_internet_show_values_label = Label(total_internet_and_time_analysis, text=internet, font=("Arial", 20), foreground="gray5")
    total_internet_show_values_label.grid(row=1, column=1)
    total_time_label = Label(total_internet_and_time_analysis, text="Total Time used today:     ",
                                 font=("Arial", 20), foreground="gray5")
    total_time_label.grid(row=2, column=0)
    total_time_show_values_label = Label(total_internet_and_time_analysis, text=total_time, font=("Arial", 20),
                                             foreground="gray5")
    total_time_show_values_label.grid(row=2, column=1)

    create_graphs_button = customtkinter.CTkButton(total_day_analysis_window, text="Generate Graphs",
                                                   corner_radius=10,
                                                   width=500,
                                                   font=("Arial", 17, "bold"), command=generate_the_required_graphs_of_day_analysis)

    create_graphs_button.pack(anchor=CENTER)


def main_process_unit():
    # all background calculations must happen in this function
    global analysis_window
    global prev_bytes_init_start_internet_sent
    global prev_bytes_init_start_internet_received
    global time_limit_future_bind
    global min_average_internet_distribution, avg_internet, predicted_time_for_internet_usage, internet_used, data_grant_list
    if analysis_window.winfo_exists() == 1:  # before when key.hook was in while loop it consumed staggering 1 to infinite amount of memory and then the solution which I got was this, and now decrease from 1 to 4 gb memory consumption to 36.7 to 40 mb memory consumption!
        keyboard.hook(on_key_event_for_quick_close)
    if analysis_window.winfo_exists() == 0:
        keyboard.unhook(on_key_event_for_quick_close)
    while analysis_window.winfo_exists() == 1:  # Runs only if analysis window is open
        if analysis_window.winfo_exists() == 1:
            # if Analysis window exists then monitor subprocesses should run
            internet_used = round(float(total_internet_been_used(prev_bytes_init_start_internet_sent, prev_bytes_init_start_internet_received)), 3)  # processes the internet used till now after a new session
            # print(internet_used)  prints internet used
            check_internet(current_internet=internet_used)  # Checks if internet limit reached or not
            current_time = current_total_time_in_seconds()  # processes the current time in seconds
            time_used_check(current_time=current_time)  # Checks if the time limit reached or not
            time_in_sec_left = time_limit_future_bind - current_time  # This variable over here gives the left time for destroying the analysing window
            # print(time_in_sec_left) prints time left in seconds
            time_left_in_pov_of_time_limit = int(time_limit_Entry.get())-time_in_sec_left
            avg_internet = internet_used/(time_left_in_pov_of_time_limit+0.00000000001)
            min_average_internet_distribution = int(internet_limit_Entry.get())/int(time_limit_Entry.get())
            total_internet_left_ = (int(internet_limit_Entry.get()) + int(sum(data_grant_list)) - internet_used)
            if avg_internet != 0:
                predicted_time_for_internet_usage = str(math.floor(total_internet_left_/avg_internet))
            elif avg_internet == 0:
                predicted_time_for_internet_usage = "Infinite"
            update_show_values_column(internet_value=internet_used, time_value=time_in_sec_left, avg_internet_value=str(avg_internet), predicted_internet_finish_time=predicted_time_for_internet_usage)
            time.sleep(wait_duration_in_main_unit)  # sleeping a very less time will affect the program negligibly, and also it will use less memory, so now its time efficient and memory efficient algorithm

        else:
            break
    note_total_data_used_the_following_day(internet_used_in_this_session=internet_used,
                                           time_used_in_this_session=time_left_in_pov_of_time_limit)
    note_internet_and_time_and_extend___list____format_____for_graphing(internet_used_in_this_session=internet_used,
                                                                        time_used_in_this_session=time_left_in_pov_of_time_limit,
                                                                        average_internet_usage_rate=avg_internet)
    print("Successfully noted the time and internet used in this session.")


def reset_password():
    global new_password_entry_field, re_password_entry_field
    new_kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,  # 32 bytes for Fernet key
        salt=b'hash crack',
        iterations=100000,  # You can adjust the number of iterations
        backend=default_backend()
    )
    if new_password_entry_field.get() == re_password_entry_field.get():
        new_key = base64.urlsafe_b64encode(new_kdf.derive((new_password_entry_field.get()).encode()))
        # print(new_key)
        double_hashed_key = double_encryption_key_generator(value=new_key.decode())
        print("Double hashed password - ", double_hashed_key)
        with open("Doubly hashed master key.enc", 'wb') as hashed_master_key__reset__:
            hashed_master_key__reset__.write(double_hashed_key)
        ###############################
        open("Browser automation software stored encrypted files/encrypted clipboards/encrypted clipboards.enc",
             'wb').close()
        delete_all_files__mentioned(___directory___="Browser automation software stored encrypted files/Encrypted screenshots")
        delete_all_files__mentioned(___directory___="Browser automation software stored encrypted files/Encrypted Authentication Details")
        delete_all_files__mentioned(___directory___="Browser automation software stored encrypted files/Encrypted screenrecords")
        delete_all_files__mentioned(___directory___="Browser automation software stored encrypted files/Encrypted written notes")
        ################################
        delete_all_folders_excluding_general_folder()
        ################################
        delete_all_files__mentioned(___directory___="Browser automation important cache files/image instead of video cache data")
        delete_all_files__mentioned(___directory___="Browser automation important cache files/modification image detection list details")
        #################################
        delete_all_files__mentioned(___directory___="To-do list folder")
        print("New Log-in key Saved")
        Input_Window.destroy()
        print("Successfully changed the password")
    else:
        print("Error: The re-entered password is wrong")
        new_password_entry_field.delete(0, END)
        re_password_entry_field.delete(0, END)

def delete_all_folders_excluding_general_folder():
    all_folder_files_in_dir = os.listdir("Folder Holding Files/")
    for delete in range(len(all_folder_files_in_dir)):
        if all_folder_files_in_dir[delete] != "General( B A S ).pkl":
            os.remove("Folder Holding Files/" + str(
                all_folder_files_in_dir[delete]))


def delete_all_files__mentioned(___directory___):
    files_to_delete = os.listdir(
        str(___directory___))
    for delete in range(len(files_to_delete)):
        os.remove(str(___directory___) + "/" + str(
            files_to_delete[delete]))



def pop_up_reset_password_window():
    global reset_password_window, new_password_entry_field, re_password_entry_field
    reset_password_window = Toplevel(Input_Window)
    reset_password_window.title("Reset Password")
    reset_password_window.minsize(width=800, height=225)
    reset_password_window.maxsize(width=800, height=225)
    Label(reset_password_window, text="! You're Previous data will be lost !", font=("Courier", 20, "bold"), fg="orange").pack(anchor="center")
    reset_password_frame = Frame(reset_password_window)
    reset_password_frame.pack(anchor=CENTER, pady=20)
    Label(reset_password_frame, text="Password Entered", font=("Courier", 15, "bold"), fg="gray4").grid(row=0, column=0, padx=10)
    Label(reset_password_frame, text="Password Re-entered", font=("Courier", 15, "bold"), fg="gray4").grid(row=0, column=1, padx=10)
    new_password_entry_field = customtkinter.CTkEntry(reset_password_frame, font=("Arial", 15, "bold"), width=200, placeholder_text="Password", show="#")
    new_password_entry_field.grid(row=1, column=0)
    re_password_entry_field = customtkinter.CTkEntry(reset_password_frame, font=("Arial", 15, "bold"), width=200, placeholder_text="re-enter Password")
    re_password_entry_field.grid(row=1, column=1)
    new_password_button = customtkinter.CTkButton(reset_password_window, text="Confirm Password reset",  font=("Courier", 20, "bold"), fg_color="red", hover_color="red3",  command=reset_password, width=500)
    new_password_button.pack(anchor=CENTER)


def get_screenshot_compress_it_and_encrypt_it_and_send_those_bytes(x1, y1, x2, y2):
    # grabs screenshot, encrypts it and compresses it and saves the screenshot bytes and also dimensions in a separate file
    global encrypter, matching_key_hashed, refactored_paths
    key = key_derive()
    if double_encryption_key_generator(value=(key.decode())) == matching_key_hashed:
        if x2 > x1 and y2 > y1:

            curr_time = time.localtime()
            curr_clock = time.strftime("%H-%M-%S", curr_time)
            screenshot = ImageGrab.grab(bbox=(x1, y1, x2, y2))  # Capture a region from (0,0) to (800,600))
            time_tag_file_name_format = str(datetime.date.today())+"-"+str(curr_clock)
            buffer = io.BytesIO()
            screenshot.save(buffer, format='PNG')
            image_data = buffer.getvalue()
            encrypted_image = encrypter.encrypt(image_data)
            compressed_image_bytes = zlib.compress(encrypted_image, level=9)
            with open('Browser automation software stored encrypted files/Encrypted screenshots/'+time_tag_file_name_format+'.bsteci', 'wb') as file:
                file.write(compressed_image_bytes)
            print("Image Successfully Encrypted and Stored")
            refactored_paths = os.listdir("Browser automation software stored encrypted files/Encrypted screenshots")  # new
        else:
            print("Error:Dimensions are invalid")


def delete_particular_screenshot_path_from_every_folder_files(index_of_screenshot):
    global screenshots_paths, folder_file_name
    deleting_folder_file_name = refactored_paths[index_of_screenshot]
    folder_files_present = os.listdir("Folder Holding Files")
    folder_files_present.pop(folder_files_present.index("General( B A S ).pkl"))
    for number_of_folder_files in range(len(folder_files_present)):
        with open("Folder Holding Files/"+folder_files_present[number_of_folder_files], "rb") as particular_folder_file__extraction_mode__:
            folder_file_screenshot_Data_in_it = list(pickle.load(particular_folder_file__extraction_mode__)["paths"])
            check_if_it_has_deleting_file_name_in_it = folder_file_screenshot_Data_in_it.count(deleting_folder_file_name)
            if check_if_it_has_deleting_file_name_in_it == 1:
                del folder_file_screenshot_Data_in_it[folder_file_screenshot_Data_in_it.index(deleting_folder_file_name)]
                deleted_path_data = {
                    "paths": folder_file_screenshot_Data_in_it
                }
                with open("Folder Holding Files/" + folder_files_present[number_of_folder_files], "wb") as remove_screenshot_path_folder_file000:
                    pickle.dump(deleted_path_data, remove_screenshot_path_folder_file000)



def delete_screenshot_function_only_window_open():
    global index_value_init, screenshots_paths, folder_file_name
    if folder_file_name == "General( B A S ).pkl":
        os.remove("Browser automation software stored encrypted files/Encrypted screenshots/"+str(screenshots_paths[index_value_init]))
        delete_particular_screenshot_path_from_every_folder_files(index_of_screenshot=index_value_init)
        del screenshots_paths[index_value_init]
    else:
        del refactored_paths[index_value_init]
        deleted_path_data = {
            "paths": refactored_paths
        }
        with open("Folder Holding Files/" + str(folder_file_name), "wb") as remove_screenshot_path_folder_file:
            pickle.dump(deleted_path_data, remove_screenshot_path_folder_file)

    if index_value_init == len(screenshots_paths):
        index_value_init -= 1
    if index_value_init < len(screenshots_paths):
        if index_value_init > 0:
            index_value_init -= 1
        if index_value_init < 0:
            if index_value_init > (-1*len(screenshots_paths)):
                index_value_init += 1
    decrypt_images_(index_value_init)





def right_positive_index_change():
    global index_value_init, screenshots_paths
    try:
        if index_value_init < (len(screenshots_paths)):
            index_value_init += 1
            decrypt_images_(index_value_init)
        else:
            index_value_init = 0
            decrypt_images_(index_value_init)
    except:
        index_value_init = 0
        decrypt_images_(index_value_init)



def left_negative_index_change():
    global index_value_init, screenshots_paths
    try:
        if index_value_init > (-1*len(screenshots_paths)):
            index_value_init -= 1
            decrypt_images_(index_value_init)
        else:
            index_value_init = len(screenshots_paths)-1
            decrypt_images_(index_value_init)
    except:
        pass



def decrypt_images_(index_value):
    global decrypter111, screenshots_paths, decrypted_image_show_label, decrypted_image, main_frame_in_video_player, index_level_show_label, folder_file_name, tk_image, decrypted_data, original_width_image, original_height_image, zoom_in_count
    zoom_in_count = 0
    decrypted_image_show_label.delete()
    index_level_show_label.configure(text=str((str(screenshots_paths.index(str(screenshots_paths[index_value]))+1)+" of "+str(len(screenshots_paths)))+" in '"+str(folder_file_name[0:-13])+ "' Folder "))
    decrypt_image_globally(index_value_=index_value)
    original_width_image = decrypted_image.width
    original_height_image = decrypted_image.height
    tk_image = ImageTk.PhotoImage(decrypted_image)
    disl_w = 960.0
    disl_h = 495.5
    decrypted_image_show_label.create_image(disl_w, disl_h, anchor="center", image=tk_image)
    decrypted_image_show_label.image = tk_image  # Keeping a reference
    # decrypted_image_show_label.pack(anchor="center")

def decrypt_image_globally(index_value_):
    global decrypted_image
    key = key_derive()
    decrypter____ = Fernet(key)
    with open('Browser automation software stored encrypted files/Encrypted screenshots/' + screenshots_paths[index_value_],
              'rb') as file:
        file_data = file.read()
    decompressed_data = zlib.decompress(file_data)
    decrypted_data = decrypter____.decrypt(decompressed_data)
    decrypted_image = Image.open(io.BytesIO(decrypted_data))

def save_current_displayed_image():
    global decrypted_image
    # Get the file path to save the image
    file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                             filetypes=[("PNG files", "*.png"),
                                                        ("JPEG files", "*.jpg"),
                                                        ("All files", "*.*")])

    # Check if a file path is selected
    if file_path:
        # Save the image to the selected file path
        decrypted_image.save(file_path)
        print(f"Current image successfully saved to: {file_path}")

def zoom_in():
    global tk_image, decrypted_image, decrypted_image_show_label, decrypted_data, original_width_image, original_height_image, zoom_in_count
    if zoom_in_count != 6:
        width_of_image = int(decrypted_image.width * 1.2)
        height_of_image = int(decrypted_image.height * 1.2)
        decrypted_image_show_label.delete()
        decrypted_image = decrypted_image.resize((width_of_image, height_of_image))
        tk_image = ImageTk.PhotoImage(decrypted_image)
        disl_w = 960.0
        disl_h = 495.5
        decrypted_image_show_label.create_image(disl_w, disl_h, anchor="center", image=tk_image)
        decrypted_image_show_label.image = tk_image  # Keeping a reference
        zoom_in_count += 1

def zoom_out():
    global tk_image, decrypted_image, decrypted_image_show_label, decrypted_data, original_width_image, original_height_image, zoom_in_count
    if zoom_in_count != 0:
        width_of_image = int(decrypted_image.width / 1.2)
        height_of_image = int(decrypted_image.height / 1.2)
        decrypted_image_show_label.delete()
        decrypted_image = decrypted_image.resize((width_of_image, height_of_image))
        tk_image = ImageTk.PhotoImage(decrypted_image)
        disl_w = 960.0
        disl_h = 495.5
        decrypted_image_show_label.create_image(disl_w, disl_h, anchor="center", image=tk_image)
        decrypted_image_show_label.image = tk_image  # Keeping a reference
        zoom_in_count -= 1


def pop_up_decrypt_encrypted_screenshot_image_window():
    global matching_key_hashed, decrypter111, screenshots_paths, decrypted_image_show_label, decrypted_image, main_frame_in_video_player, index_value_init, index_level_show_label, get_index_and_show_image_Entry, excluding_index_entry_from_random_show, folder_file_name
    global folder_index_entry_field, image_index_for_folder_entry_field
    key = key_derive()
    if double_encryption_key_generator(value=(key.decode())) == matching_key_hashed:
        x_pos, y_pos = pyautogui.size()
        # print(y_pos, x_pos)
        index_value_init = 0
        decrypter_key = key  # initialising encrypter
        decrypter111 = Fernet(decrypter_key)
        screenshots_paths = refactored_paths
        main_frame_in_video_player = Toplevel(Input_Window, background="green4")
        main_frame_in_video_player.title("Decrypted image viewer")
        display_actions_frame = Frame(main_frame_in_video_player)
        display_actions_frame.pack(anchor="center", pady=10)
        index_level_show_label = customtkinter.CTkLabel(display_actions_frame, text="Some error", font=("Courier", 20, "bold"), fg_color="black", text_color="white", bg_color="green4", corner_radius=50, padx=30)
        index_level_show_label.grid(row=0, column=0)

        folder_view = customtkinter.CTkButton(main_frame_in_video_player, text="View Folders",
                                              width=80,
                                              font=("Arial", 20, "bold"), bg_color="green4", command=pop_up_folder_files_window)
        folder_view.place(x=10, y=8)
        save_image_button = customtkinter.CTkButton(main_frame_in_video_player, text="Save image",
                                                    width=80,
                                                    font=("Arial", 20, "bold"), bg_color="green4", command=save_current_displayed_image)
        save_image_button.place(x=1390, y=8)
        # folder_name_label_for_display = customtkinter.CTkLabel(image_viewer, text=folder_file_name, font=("Arial", 20),text_color="white",  fg_color="gray5", corner_radius=50)
        # folder_name_label_for_display.place(x=50, y=8)
        display_image_frame = Frame(main_frame_in_video_player)
        display_image_frame.pack(anchor=CENTER)
        decrypted_image_show_label = Canvas(display_image_frame, height=925, width=1900, background="black")
        decrypted_image_show_label.pack(anchor=CENTER)
        decrypt_images_(index_value=index_value_init)
        image_viewer_Buttons_frame = LabelFrame(main_frame_in_video_player, padx=50, pady=5)
        image_viewer_Buttons_frame.place(x=int(x_pos/8), y=(y_pos-175))
        showing_action_frame = Frame(image_viewer_Buttons_frame)
        showing_action_frame.grid(row=0, column=0, padx=15)
        movement_action_frame = Frame(image_viewer_Buttons_frame)
        movement_action_frame.grid(row=0, column=3, padx=15)
        random_action_frame = Frame(image_viewer_Buttons_frame)
        random_action_frame.grid(row=0, column=4, padx=20)
        # folder_creation_action_frame = Frame(image_viewer_Buttons_frame)
        # folder_creation_action_frame.grid(row=0, column=5, padx=20)
        add_to_specific_folder_frame = Frame(image_viewer_Buttons_frame)
        add_to_specific_folder_frame.grid(row=0, column=5, padx=15)
        zoom_functions = Frame(image_viewer_Buttons_frame)
        zoom_functions.grid(row=0, column=6, padx=15)
        more_info_label(
            tooltip_Text="Enter the index in this entry only in the form of xyz; The image allotted to that index will be shown.",
            window=main_frame_in_video_player, abscissa=280, ordinate=925, Wrap_l=400, side_left_distance_y=0,
            side_left_distance_x=0, side="right")
        more_info_label(tooltip_Text="Enter the index in this entry only in the form of x,y,z; These values will be excluded when random button is clicked.", window=main_frame_in_video_player, abscissa=805, ordinate=925, Wrap_l=400, side_left_distance_y=0, side_left_distance_x=0, side="right")
        more_info_label(
            tooltip_Text="Enter the folder index in first entry only in the form of abc. In the second entry enter the index values of images in the form of x,y,z",
            window=main_frame_in_video_player, abscissa=1068, ordinate=925, Wrap_l=400, side_left_distance_y=100,
            side_left_distance_x=400, side="left")
        # showing_action_frame.grid(row=0, column=3)
        get_index_and_show_image_Entry = customtkinter.CTkEntry(showing_action_frame, width=80, font=("Arial", 20, "bold"), corner_radius=10, placeholder_text="Index")
        get_index_and_show_image_Entry.grid(row=0, column=0)
        get_index_and_show_image_button = customtkinter.CTkButton(showing_action_frame, text="Show", font=("Arial", 20, "bold"), command=get_value_from_index_of_images_and_display, corner_radius=10, width=80)
        get_index_and_show_image_button.grid(row=0, column=1)
        left_button = customtkinter.CTkButton(movement_action_frame, text="<", font=("Arial", 30, "bold"), command=left_negative_index_change, corner_radius=10, width=5)
        left_button.grid(row=0, column=0)
        right_button = customtkinter.CTkButton(movement_action_frame, text=">", font=("Arial", 30, "bold"), command=right_positive_index_change, corner_radius=10, width=5)
        right_button.grid(row=0, column=2)
        force_close_button = customtkinter.CTkButton(movement_action_frame, text="X", font=("Arial", 30, "bold"), command=main_frame_in_video_player.destroy, corner_radius=10, fg_color="red2", width=5, hover_color="red3")
        force_close_button.grid(row=0, column=1, padx=2)
        delete_screenshot_button = customtkinter.CTkButton(image_viewer_Buttons_frame, text="Delete", corner_radius=10, fg_color="red2", width=80, hover_color="red3",
                                    font=("Arial", 20, "bold"), command=delete_screenshot_function_only_window_open)
        delete_screenshot_button.grid(row=0, column=2)
        get_random_image_button = customtkinter.CTkButton(random_action_frame, text="Random", font=("Arial", 20, "bold"), command=get_random_image, corner_radius=10, fg_color="purple3", width=80, hover_color="purple")
        get_random_image_button.grid(row=0, column=1)
        excluding_index_entry_from_random_show = customtkinter.CTkEntry(random_action_frame, font=("Arial", 20, "bold"), width=80, placeholder_text="Index", corner_radius=10)
        excluding_index_entry_from_random_show.grid(row=0, column=0)

        folder_index_entry_field = customtkinter.CTkEntry(add_to_specific_folder_frame, width=150,
                                                                  font=("Arial", 20, "bold"),
                                                                  corner_radius=10, placeholder_text="Folder Index")
        folder_index_entry_field.grid(row=0, column=0)

        image_index_for_folder_entry_field = customtkinter.CTkEntry(add_to_specific_folder_frame, width=150,
                                                           font=("Arial", 20, "bold"),
                                                           corner_radius=10, placeholder_text="Image Index")
        image_index_for_folder_entry_field.grid(row=0, column=1)

        add_to_folder_button = customtkinter.CTkButton(add_to_specific_folder_frame, text="Add +", corner_radius=10,
                                                       width=80,
                                                       font=("Arial", 20, "bold"), command=get_folder_index_and_image_index_and_process_it)
        add_to_folder_button.grid(row=0, column=2)
        zoom_in_button = customtkinter.CTkButton(zoom_functions, text="zoom+", corner_radius=10,
                                                       width=80,
                                                       font=("Arial", 20, "bold"), command=zoom_in)
        zoom_in_button.grid(row=0, column=0)
        zoom_out_button = customtkinter.CTkButton(zoom_functions, text="zoom-", corner_radius=10,
                                                 width=80,
                                                 font=("Arial", 20, "bold"), command=zoom_out)
        zoom_out_button.grid(row=0, column=1)
        decrypted_image_show_label.scale_factor = 1.0
        decrypted_image_show_label.bind('<ButtonPress-1>', lambda event: decrypted_image_show_label.scan_mark(event.x, event.y))
        decrypted_image_show_label.bind("<B1-Motion>", lambda event: decrypted_image_show_label.scan_dragto(event.x, event.y, gain=1))


def get_value_from_index_of_images_and_display():
    global screenshots_paths, get_index_and_show_image_Entry, index_value_init
    try:
        image_index_entered = int(get_index_and_show_image_Entry.get())
        if (image_index_entered-1) < len(screenshots_paths):
            if image_index_entered > 0:
                index_value_init = image_index_entered-1
                decrypt_images_(index_value_init)
    except:
        print("Error: Invalid Entry")
        get_index_and_show_image_Entry.delete(0, "end")


def get_random_image():
    global screenshots_paths, index_value_init, excluding_index_entry_from_random_show
    index_exclusion_str = excluding_index_entry_from_random_show.get()
    index_exclusion_str_last_isolation = index_exclusion_str+",0"
    index_value_list = []
    if index_exclusion_str == "":
        random_int_btw = random.randrange(0, len(screenshots_paths))
        index_value_init = random_int_btw
        decrypt_images_(index_value=index_value_init)
    elif index_exclusion_str.isspace() is False:
        previous_index = 0
        for comma_separate in range(len(index_exclusion_str_last_isolation)):
            if index_exclusion_str_last_isolation[comma_separate] == ",":
                the_index_for_exclusion = index_exclusion_str_last_isolation[previous_index:comma_separate]
                previous_index = comma_separate+1
                try:
                    index_value_list.append((int(the_index_for_exclusion)-1))
                except:
                    excluding_index_entry_from_random_show.delete(0, "end")
    random_int_btw = random.randrange(0, len(screenshots_paths))
    index_value_init = random_int_btw

    while index_value_init in index_value_list:
        random_int_btw = random.randrange(0, len(screenshots_paths))
        index_value_init = random_int_btw
    # print(random_int_btw)
    decrypt_images_(index_value=index_value_init)

def add_task_and_expire_date_and_time_to_it():
    global add_task_entry, done_task_index_entry
    random_text = random.randrange(0, 999)
    curr_time = time.localtime()
    curr_date = str(datetime.date.today())
    curr_clock = time.strftime("%H-%M-%S", curr_time)
    time_tag_file_name_format = str(datetime.date.today()) + "-" + curr_date + "-" +str(curr_clock)
    file_name = "Task at " + time_tag_file_name_format + " " +str(random_text) +" ( B A S).pkl"
    task = str(add_task_entry.get())+" "
    if task.isspace() is False:
        task = "Created at - '" + curr_date+ "', Task: " + task
        task_file_data___ = {
            "task_text": task,
        }
        with open("To-do list folder/"+file_name, "wb") as task_file_initializer:
            pickle.dump(task_file_data___, task_file_initializer)
        print("Successfully added the task")
        refresh_task_list_and_show_task()
    else:
        print("Error: Not filled all entries.")


def refresh_task_list_and_show_task():
    global to_do_list, total_task_left
    to_do_list.delete(0, END)
    total_tasks = os.listdir("To-do list folder/")
    total_task_left.config(text="Total Tasks left - "+str(len(total_tasks))+" Left")
    for number_of_tasks in range(len(total_tasks)):
        with open("To-do list folder/"+total_tasks[number_of_tasks], "rb") as loading_task_data:
            task_whole_data = pickle.load(loading_task_data)
            task_text___ = task_whole_data["task_text"]
        to_do_list.insert(END, str(number_of_tasks) + ": " + task_text___)


def done_task_list():
    global done_task_index_entry
    index_for_done_task = str(done_task_index_entry.get())
    total_tasks = os.listdir("To-do list folder/")
    if index_for_done_task.isnumeric() is True:
        os.remove("To-do list folder/"+total_tasks[int(index_for_done_task)])
        print("Task Done")
    if index_for_done_task == "all":
        for total_task_deletion in range(len(total_tasks)):
            os.remove("To-do list folder/"+total_tasks[total_task_deletion])
        print("All Tasks Done")
    refresh_task_list_and_show_task()



def pop_up_TO_DO_window():
    global add_task_entry, done_task_index_entry, expire_date_entry, expire_time_entry, to_do_list, total_task_left
    try:
        to_do_l_window = Toplevel(Input_Window)
        to_do_l_window.title("To-Do list")
        to_do_l_window.minsize(width=1125, height=410)
        to_do_l_window.maxsize(width=1125, height=410)
        total_task_left = Label(to_do_l_window,
                                            text=("Error"),
                                            font=("Arial", 15, "bold"))
        total_task_left.pack(anchor="center", pady=10)
        main_to_do_window_frame = Frame(to_do_l_window, pady=20)
        main_to_do_window_frame.pack(anchor=CENTER)
        add_task_frame = Frame(main_to_do_window_frame)
        add_task_frame.grid(row=0, column=0, padx=30, pady=10)
        task_done_frame = Frame(main_to_do_window_frame)
        task_done_frame.grid(row=0, column=2, padx=30, pady=10)



        add_task_entry = customtkinter.CTkEntry(add_task_frame, width=200,
                                                                  font=("Arial", 15, "bold"),
                                                                  corner_radius=50, placeholder_text="Task")
        add_task_entry.grid(row=0, column=0)
        add_task_button = customtkinter.CTkButton(add_task_frame, text="Add Task",
                                                       corner_radius=10,
                                                       width=80,
                                                       font=("Arial", 13, "bold"), command=add_task_and_expire_date_and_time_to_it)
        add_task_button.grid(row=0, column=1)
        done_task_index_entry = customtkinter.CTkEntry(task_done_frame, font=("Courier", 15, "bold"),
                                                                 corner_radius=50, width=75, placeholder_text="Index")
        done_task_index_entry.grid(row=0, column=0)
        done_task_get_button = customtkinter.CTkButton(task_done_frame, text="Done",
                                                                font=("Arial", 13, "bold"), width=80, command=done_task_list)
        done_task_get_button.grid(row=0, column=1)


        scroll_bar999 = Scrollbar(to_do_l_window)
        scroll_bar999.pack(side=RIGHT, fill=Y)
        scroll_bar111 = Scrollbar(to_do_l_window)
        # scroll_bar111.pack(side=LEFT, fill=X)
        to_do_list = Listbox(to_do_l_window, yscrollcommand=scroll_bar999.set, width=90, height=10,
                                   font=("Arial", 10), borderwidth=2)
        scroll_bar999.config(command=to_do_list.yview)
        scroll_bar111.config(command=to_do_list.xview)
        to_do_list.pack(padx=30)
        # insert_folder_name_with_index()
        refresh_task_list_and_show_task()
    except:
        print("Error: Can't open To-Do list")


def double_encryption_key_generator(value):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,  # 32 bytes for Fernet key
        salt=b'hash crack',
        iterations=100000,  # You can adjust the number of iterations
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive((value).encode()))
    return key

def clear_notes():
    global writing_area_widget
    writing_area_widget.delete(0.0, END)

def copy_notes():
    global writing_area_widget
    copy_this_much_text = str(writing_area_widget.get(0.0, END)) + " "
    if copy_this_much_text.isspace() is False:
        pyperclip.copy(copy_this_much_text)
    else:
        print("There is Nothing written")

def save_notes__as__text_file():
    global writing_area_widget, name_to_save_entry_field
    notes_file_name = str(name_to_save_entry_field.get()) + " "
    n = notes_file_name
    written_text = str(writing_area_widget.get(0.0, END)) + " "
    if notes_file_name.isspace() is False:
        notes_file_name = "All text files from TakeNote//" + notes_file_name + "( b a s ) ( text ).txt"
        if written_text.isspace() is False:
            with open(notes_file_name, "w") as write_File:
                write_File.write(written_text)
            print(" Text saved successfully as ", n )
        else:
            print("There is Nothing written")
    else:
        print("Error: No file name provided.")




def save_in_notes__encrypted__():
    global writing_area_widget, name_to_save_entry_field
    key = key_derive()
    if double_encryption_key_generator(value=key.decode()) == matching_key_hashed:
        notes_file_name = str(name_to_save_entry_field.get()) + " "
        written_text = str(writing_area_widget.get(0.0, END)) + " "
        if notes_file_name.isspace() is False:
            notes_file_name = "Browser automation software stored encrypted files/Encrypted written notes//" + notes_file_name + "( b a s ) (     encrypted ).basne"
            if written_text.isspace() is False:
                cypher_suit = Fernet(key)
                with open(notes_file_name, "wb") as write_File_as_bytes:
                    encrypted_text = cypher_suit.encrypt(written_text.encode())
                    written_text_in_bytes = bytes(encrypted_text)
                    compressed_bytes_written_bytes = zlib.compress(written_text_in_bytes)
                    write_File_as_bytes.write(compressed_bytes_written_bytes)
                    # decom = zlib.decompress(compressed_bytes_written_bytes)
                    # decode = decom.decode()
                    # print(decode)
            else:
                print("There is Nothing written")
        else:
            print("Error: No file name provided.")
    else:
        print("Error: Invalid password")
    refresh_and_insert_notes_with_name_in_the_notes_name_displayer_window()


def refresh_and_insert_notes_with_name_in_the_notes_name_displayer_window():
    global show_notes_list, encrypted_written_text_paths, total_notes_present_label, all_notes_files_compiled_one_without_full__paths, all_notes_files_compiled_full_paths
    show_notes_list.delete(0, END)
    # not_encrypted_written_text__full__paths__ = []
    encrypted_written_text__full__paths__ = []
    # not_encrypted_written_text_paths = os.listdir("notes save in ( not encrypted )")
    # for none_encrypted___ in range(len(not_encrypted_written_text_paths)):
    #     not_encrypted_written_text__full__paths__.append("notes save in ( not encrypted )/"+not_encrypted_written_text_paths[none_encrypted___])
    encrypted_written_text_paths = os.listdir(
        "Browser automation software stored encrypted files/Encrypted written notes")
    for _____encrypted___ in range(len(encrypted_written_text_paths)):
        encrypted_written_text__full__paths__.append("Browser automation software stored encrypted files/Encrypted written notes/"+encrypted_written_text_paths[_____encrypted___])
    all_notes_files_compiled_one_without_full__paths = encrypted_written_text_paths
    all_notes_files_compiled_full_paths = encrypted_written_text__full__paths__
    total_notes_present_label.config(text="Total Notes -  " + str(len(all_notes_files_compiled_one_without_full__paths)))
    # print(all_notes_files_compiled_full_paths)
    for number_of_notes in range(len(all_notes_files_compiled_one_without_full__paths)):
        show_notes_list.insert(END, str(number_of_notes)+ " : " + all_notes_files_compiled_one_without_full__paths[number_of_notes][:-34])


def delete_notes():
    global all_notes_files_compiled_full_paths, index_of_notes_to_delete_entry, take_notes_to_be_displayed_window
    index_____ = index_of_notes_to_delete_entry.get()
    if str(index_____).isnumeric() is True:
        os.remove(all_notes_files_compiled_full_paths[int(index_____)])
        refresh_and_insert_notes_with_name_in_the_notes_name_displayer_window()


def open_notes():
    global all_notes_files_compiled_full_paths, writing_area_widget, name_to_save_entry_field, index_of_notes_to_open_entry
    get_index = index_of_notes_to_open_entry.get()
    if str(get_index).isnumeric() is True:
        get_index = int(get_index)
        notes_reffered_to = all_notes_files_compiled_full_paths[get_index]
        if notes_reffered_to[-5:] == "basne":
            key = key_derive()
            cypher_suit = Fernet(key)
            with open(notes_reffered_to, "rb") as encrypted_notes_file:
                written_compressed_notes = encrypted_notes_file.read()
                decompressed_notes = zlib.decompress(written_compressed_notes)
                decrypted_notes = cypher_suit.decrypt(decompressed_notes).decode()
                notes = decrypted_notes
                name_to_save_entry_field.delete(0, END)
                name_to_save_entry_field.insert(0, str(notes_reffered_to[75:-34]))
        else:
            with open(notes_reffered_to, "rb") as not_encrypted_notes_file:
                written_compressed_notes = not_encrypted_notes_file.read()
                decompressed_notes = zlib.decompress(written_compressed_notes)
                notes = decompressed_notes.decode()
                name_to_save_entry_field.delete(0, END)
                name_to_save_entry_field.insert(0, str(notes_reffered_to[32:-34]))
        clear_notes()
        writing_area_widget.insert(END, notes)


def pop_up_show_notes_files():
    global takenotes_window, show_notes_list, not_encrypted_written_text_paths, encrypted_written_text_paths, total_notes_present_label, index_of_notes_to_delete_entry, take_notes_to_be_displayed_window, index_of_notes_to_open_entry
    if double_encryption_key_generator(value=key_derive().decode()) == matching_key_hashed:
            take_notes_to_be_displayed_window = Toplevel(takenotes_window)
            take_notes_to_be_displayed_window.title("All notes")
            take_notes_to_be_displayed_window.minsize(width=1125, height=410)
            take_notes_to_be_displayed_window.maxsize(width=1125, height=410)
            total_notes_present_label = Label(take_notes_to_be_displayed_window,
                                                text="Total Notes -  " + "0", font=("Arial", 15, "bold"))
            total_notes_present_label.pack(anchor="center", pady=10)
            index_get_notes_frame = Frame(take_notes_to_be_displayed_window, pady=20)
            index_get_notes_frame.pack(anchor=CENTER)
            # create_folder_frame = Frame(index_get_folder_frame)
            # create_folder_frame.grid(row=0, column=0, padx=40, pady=10)
            delete_notes_frame = Frame(index_get_notes_frame)
            delete_notes_frame.grid(row=0, column=1, padx=40, pady=10)

            open__notes__frame = Frame(index_get_notes_frame)
            open__notes__frame.grid(row=0, column=2, padx=40, pady=10)
            index_of_notes_to_delete_entry = customtkinter.CTkEntry(delete_notes_frame, font=("Courier", 15, "bold"), corner_radius=50, width=75, placeholder_text="Index")
            index_of_notes_to_delete_entry.grid(row=0, column=0)
            get_notes_index_for_deletion__button__ = customtkinter.CTkButton(delete_notes_frame, text="Delete", font=("Arial", 13, "bold"), width=80, command=delete_notes)
            get_notes_index_for_deletion__button__.grid(row=0, column=1)

            index_of_notes_to_open_entry = customtkinter.CTkEntry(open__notes__frame, font=("Courier", 15, "bold"),
                                                                     corner_radius=50, width=75,
                                                                     placeholder_text="Index")
            index_of_notes_to_open_entry.grid(row=0, column=0)
            get_notes_index_for_opening__button__ = customtkinter.CTkButton(open__notes__frame, text="Open notes",
                                                                    font=("Arial", 13, "bold"), width=80,
                                                                    command=open_notes)
            get_notes_index_for_opening__button__.grid(row=0, column=1)

            scroll_bar_of_notes_section = Scrollbar(take_notes_to_be_displayed_window)
            scroll_bar_of_notes_section.pack(side=RIGHT, fill=Y)
            show_notes_list = Listbox(take_notes_to_be_displayed_window, yscrollcommand=scroll_bar_of_notes_section.set, width=90, height=10, font=("Arial", 10), borderwidth=2)
            scroll_bar_of_notes_section.config(command=show_notes_list.yview)
            show_notes_list.pack(padx=30)
            refresh_and_insert_notes_with_name_in_the_notes_name_displayer_window()
        # except:
        #     print("Error: Invalid password")

def pop_up_takenotes_window():
    global writing_area_widget, name_to_save_entry_field, takenotes_window
    takenotes_window = Toplevel(Input_Window)
    main_frame_window = Frame(takenotes_window)
    main_frame_window.pack(anchor=CENTER)
    all_button_widget_frame = Frame(main_frame_window)
    all_button_widget_frame.pack(anchor=CENTER, pady=20)
    takenotes_window.title("TakeNotes")
    show_all_notes_____button = customtkinter.CTkButton(all_button_widget_frame, text="Notes", font=("Arial", 13, "bold"), command=pop_up_show_notes_files)
    show_all_notes_____button.grid(row=0, column=0, padx=5)
    copy_notes_button = customtkinter.CTkButton(all_button_widget_frame, text="Copy", font=("Arial", 13, "bold"), command=copy_notes)
    copy_notes_button.grid(row=0, column=1, padx=10)
    # clear_notes_button = customtkinter.CTkButton(all_button_widget_frame, text="Clear", font=("Arial", 13, "bold"))
    # clear_notes_button.grid(row=0, column=2, padx=10)
    save_notes_frame___ = Frame(all_button_widget_frame)
    save_notes_frame___.grid(row=0, column=3, padx=10)
    name_to_save_entry_field = customtkinter.CTkEntry(save_notes_frame___, font=("Courier", 15, "bold"),
                           corner_radius=50, width=200, placeholder_text="Name")
    name_to_save_entry_field.grid(row=0, column=0)
    save_inbuilt_encrypted = customtkinter.CTkButton(save_notes_frame___, text="Save as encrypted", font=("Arial", 13, "bold"), command=save_in_notes__encrypted__)
    save_inbuilt_encrypted.grid(row=0, column=1)
    # save_inbuilt_not_encrypted = customtkinter.CTkButton(save_notes_frame___, text="Save in ", font=("Arial", 13, "bold"), command=save_in_notes_not__encrypted__)
    # save_inbuilt_not_encrypted.grid(row=0, column=2)
    save_notes_as_desktop = customtkinter.CTkButton(save_notes_frame___, text="Save as", font=("Arial", 13, "bold"), command=save_notes__as__text_file)
    save_notes_as_desktop.grid(row=0, column=3)

    # save_particular = customtkinter.CTkButton(save_notes_frame___, text="Save", font=("Arial", 13, "bold"))
    # save_particular.grid(row=0, column=4)

    clear_notes_button = customtkinter.CTkButton(all_button_widget_frame, text="All Clear", font=("Arial", 13, "bold"), command=clear_notes)
    clear_notes_button.grid(row=0, column=2, padx=10)
    writing_area_widget = customtkinter.CTkTextbox(main_frame_window, width=screen_width, height=screen_height, corner_radius=10, border_width=5, font=("Arial", 20), undo=True, autoseparators=True, maxundo=20)
    writing_area_widget.pack(anchor=CENTER, padx=30, pady=20)
    undo_notes_button = customtkinter.CTkButton(all_button_widget_frame, text="undo",
                                                font=("Arial", 13, "bold"), command=writing_area_widget.edit_undo)
    undo_notes_button.grid(row=0, column=4, padx=0)
    redo_notes_button = customtkinter.CTkButton(all_button_widget_frame, text="redo", font=("Arial", 13, "bold"),
                                                command=writing_area_widget.edit_redo)
    redo_notes_button.grid(row=0, column=5, padx=0)

def copy_all_from_text_scrapped_area():
    global displaying_scrapped_text_area_widget
    text = str(displaying_scrapped_text_area_widget.get(0.0, END)) + " "
    if text.isspace() is False:
        pyperclip.copy(text)
    else:
        print("Error: There is nothing to copy")

def text_scrapper():
    global displaying_scrapped_text_area_widget, for_text_url_entry_field, state_of_the_Website_text
    url___ = str(for_text_url_entry_field.get()) + " "
    if url___.isspace() is False:
        state_of_the_Website_text = requests.get(url___)
        if str(state_of_the_Website_text) == "<Response [200]>":
            print("successfully connected to the website for scrapping")
            soup = BeautifulSoup(state_of_the_Website_text.content, 'html.parser')
            # all_html_links = soup.find_all("a")
            all_html_text_paragraphs = soup.find_all('p')
            all_span_text = soup.find_all("span")
            displaying_scrapped_text_area_widget.delete(0.0, END)
            total  =  all_html_text_paragraphs + all_span_text
            for course in total:
                all_text_present = course.text
                displaying_scrapped_text_area_widget.insert(0.0, all_text_present)
        else:
            print("Error: failed to connect to the website")


def pop_up_text_based_webscrapper():
    global displaying_scrapped_text_area_widget, for_text_url_entry_field
    text_scrapper_window = Toplevel(Input_Window)
    text_scrapper_window.title("Text scrapper")
    widget_frame_text_scrapper = Frame(text_scrapper_window)
    widget_frame_text_scrapper.pack(anchor=CENTER)
    for_text_url_entry_field = customtkinter.CTkEntry(widget_frame_text_scrapper, font=("Courier", 15, "bold"),
                                                      corner_radius=50, width=200, placeholder_text="Url")
    for_text_url_entry_field.grid(row=0, column=0)
    text_scrapper_button = customtkinter.CTkButton(widget_frame_text_scrapper, text="Scrap",
                                                     font=("Arial", 13, "bold"), command=text_scrapper)
    text_scrapper_button.grid(row=0, column=1)
    copy_all_text_button = customtkinter.CTkButton(widget_frame_text_scrapper, text="Copy",
                                                         font=("Arial", 13, "bold"),
                                                         command=copy_all_from_text_scrapped_area)
    copy_all_text_button.grid(row=0, column=2)
    displaying_scrapped_text_area_widget = customtkinter.CTkTextbox(text_scrapper_window, width=screen_width, height=screen_height,
                                                   corner_radius=10, border_width=5, font=("Arial", 20), wrap="word")
    displaying_scrapped_text_area_widget.pack(anchor=CENTER, padx=30, pady=20)




def pop_up_visual_descriptive_writing():
    global choose_image_index, visual_element, screenshots_paths, content_of_info, title_of_info, visual_descriptive_index_level_show_label, main_frame_in_video_player, show_visual_d_index, visual_descriptive___sub_image____index__show_label, universal_image_controlling_widget, visual_descriptive_writing_window, folder_file_name
    if folder_file_name == "General( B A S ).pkl":
        if double_encryption_key_generator(value=key_derive().decode()) == matching_key_hashed:
            pop_up_decrypt_encrypted_screenshot_image_window()
            main_frame_in_video_player.destroy()
            x_pos, y_pos = pyautogui.size()
            visual_descriptive_writing_window = Toplevel(Input_Window)
            visual_descriptive_writing_window.title("Visual descriptive writing")
            visual_descriptive_index_level_show_label = customtkinter.CTkLabel(visual_descriptive_writing_window,
                                                                               text="None",
                                                                               font=("Courier", 20, "bold"),
                                                                               fg_color="black",
                                                                               text_color="white", corner_radius=50)
            visual_descriptive_index_level_show_label.pack(anchor=CENTER)
            Main_visual_descriptive_frame = Frame(visual_descriptive_writing_window)
            Main_visual_descriptive_frame.pack(anchor=CENTER)

            visual___data___frame___ = Frame(Main_visual_descriptive_frame)
            visual___data___frame___.grid(row=0, column=0, padx=50, pady=30)
            visual_element = Canvas(visual___data___frame___, height=870, width=950, background="black")
            visual_element.pack(anchor="e")
            info___data___frame___ = Frame(Main_visual_descriptive_frame)
            info___data___frame___.grid(row=0, column=1)
            title_of_info = customtkinter.CTkEntry(info___data___frame___, placeholder_text="Title", width=500 , height=50, font=("Arial", 30, "bold"))
            title_of_info.pack(anchor=CENTER, pady=20)

            content_of_info = customtkinter.CTkTextbox(info___data___frame___, width=500, height=600,
                                                   font=("Arial", 20, "italic"), border_width=5)
            content_of_info.pack(anchor=CENTER)

            image_controling_widget_Frame = Frame(visual_descriptive_writing_window)
            image_controling_widget_Frame.place(x=45, y=100)

            visual_descriptive___sub_image____index__show_label = customtkinter.CTkLabel(image_controling_widget_Frame,
                                                                                         text="None",
                                                                                         font=("Courier", 15, "bold"),
                                                                                         fg_color="black",
                                                                                         text_color="white",
                                                                                         corner_radius=50)
            visual_descriptive___sub_image____index__show_label.pack(anchor=CENTER, pady=20)

            universal_image_controlling_widget = customtkinter.CTkEntry(image_controling_widget_Frame, width=80, font=("Arial", 20, "bold"),
                                                        corner_radius=10)
            universal_image_controlling_widget.pack(anchor=CENTER, pady=20)



            show_particuler__visual_in__image_widget = customtkinter.CTkButton(image_controling_widget_Frame, text="Show", corner_radius=10,
                                                          width=80,
                                                          font=("Arial", 20, "bold"), command=show_particular_sub_visual_image)
            show_particuler__visual_in__image_widget.pack(anchor=CENTER, pady=20)



            sub_image_moving_frame = Frame(image_controling_widget_Frame)
            sub_image_moving_frame.pack(anchor=CENTER, pady=20)

            sub_left_button = customtkinter.CTkButton(sub_image_moving_frame, text="<", font=("Arial", 20, "bold"),
                                                  corner_radius=10, width=5, command=left_sub_index_visual_change)
            sub_left_button.grid(row=0, column=0)
            sub_right_button = customtkinter.CTkButton(sub_image_moving_frame, text=">", font=("Arial", 20, "bold"),
                                                   corner_radius=10, width=5,
                                                   command=right_sub_index_visual_change)
            sub_right_button.grid(row=0, column=1)

            widgets____frame = Frame(visual_descriptive_writing_window)
            widgets____frame.place(x=int(x_pos/4), y=(y_pos-135))

            image_choosing_frame = Frame(widgets____frame)
            image_choosing_frame.grid(row=0, column=0)

            show_particular_frame = Frame(widgets____frame)
            show_particular_frame.grid(row=0, column=1, padx=40)

            # Show_particular_image =

            move_left_right_frame__ = Frame(widgets____frame)
            move_left_right_frame__.grid(row=0, column=2, padx=40)


            choose_image_index = customtkinter.CTkEntry(image_choosing_frame, width=80, font=("Arial", 20, "bold"), corner_radius=10, placeholder_text="Index")
            choose_image_button = customtkinter.CTkButton(image_choosing_frame, text="Choose Image", corner_radius=10,
                                                         width=80,
                                                         font=("Arial", 20, "bold"), command=image_choosing)
            choose_image_index.grid(row=0, column=0)
            choose_image_button.grid(row=0, column=1)

            show_visual_d_index = customtkinter.CTkEntry(show_particular_frame, width=80, font=("Arial", 20, "bold"),
                                                        corner_radius=10, placeholder_text="Index")
            show_visual_d_button = customtkinter.CTkButton(show_particular_frame, text="Show", corner_radius=10,
                                                          width=80,
                                                          font=("Arial", 20, "bold"), command=show_particular_visual_descriptive_element_by_____index______)
            show_visual_d_index.grid(row=0, column=0)
            show_visual_d_button.grid(row=0, column=1)



            left_button = customtkinter.CTkButton(move_left_right_frame__, text="<", font=("Arial", 25, "bold"), corner_radius=10, width=5, command=left_negative___visual___index_change)
            left_button.grid(row=0, column=0)
            right_button = customtkinter.CTkButton(move_left_right_frame__, text=">", font=("Arial", 25, "bold"), corner_radius=10, width=5, command=right_positive____visual___index_change)
            right_button.grid(row=0, column=3)
            force_close_button = customtkinter.CTkButton(move_left_right_frame__, text="X", font=("Arial", 25, "bold"), corner_radius=10,
                                                         fg_color="red2", width=5, hover_color="red3", command=visual_descriptive_writing_window.destroy)
            force_close_button.grid(row=0, column=1, padx=2)

            delete_button = customtkinter.CTkButton(move_left_right_frame__, text="Delete", font=("Arial", 25, "bold"),
                                                         corner_radius=10,
                                                         fg_color="red2", width=5, hover_color="red3",
                                                         command=delete_visual_writing)
            delete_button.grid(row=0, column=2, padx=2)


            save_item = customtkinter.CTkButton(widgets____frame, text="Save", corner_radius=10,
                                                         width=80,
                                                         font=("Arial", 20, "bold"), command=save_visual_writing_details_in_a_file)
            save_item.grid(row=0, column=3)


            refresh_visual_descriptive_writing_index_value()

def delete_visual_writing():
    global visual_descripter_file_list, visual_writing_index
    os.remove("Browser automation software stored encrypted files/Encrypted Visual descriptive writing/"+visual_descripter_file_list[visual_writing_index])
    refresh_visual_descriptive_writing_index_value()
    right_positive____visual___index_change()



def show_particular_visual_descriptive_element_by_____index______():
    global show_visual_d_index, visual_writing_index, visual_describing_file_name, visual_descripter_file_list, visual_descriptive_index_level_show_label
    visual_writing_index = int(show_visual_d_index.get())-1
    visual_describing_file_name = visual_descripter_file_list[visual_writing_index]
    display_the_visual_descriptive_writings()
    visual_descriptive_index_level_show_label.configure(
        text=str(str(int(visual_descripter_file_list.index(visual_describing_file_name)) + 1) + " of " + str(
            len(visual_descripter_file_list))))


def refresh_visual_descriptive_writing_index_value():
    global visual_descripter_file_list
    visual_descripter_file_list = os.listdir("Browser automation software stored encrypted files/Encrypted Visual descriptive writing")
    # visual_descripter_len = len(visual_descripter_file_list)
    # refresh__visual_index_label()

def right_positive____visual___index_change():
    global visual_writing_index, visual_descripter_file_list, visual_descriptive_index_level_show_label, visual_describing_file_name
    try:
        if visual_writing_index < (len(visual_descripter_file_list)):
            visual_writing_index += 1
            # print(index_value_init)
            visual_describing_file_name = visual_descripter_file_list[visual_writing_index]
        else:
            visual_writing_index = 0
            # print(index_value_init)
            visual_describing_file_name = visual_descripter_file_list[visual_writing_index]
    except:
        visual_writing_index = 0
        # print("last image")
        visual_describing_file_name = visual_descripter_file_list[visual_writing_index]
    display_the_visual_descriptive_writings()
    visual_descriptive_index_level_show_label.configure(
        text=str(str(int(visual_descripter_file_list.index(visual_describing_file_name)) + 1) + " of " + str(
            len(visual_descripter_file_list))))



def left_negative___visual___index_change():
    global visual_writing_index, visual_descripter_file_list, visual_descriptive_index_level_show_label, visual_describing_file_name
    try:
        if visual_writing_index > (-1*len(visual_descripter_file_list)):
            visual_writing_index -= 1
            # print(index_value_init)
            visual_describing_file_name = visual_descripter_file_list[visual_writing_index]
        else:
            visual_writing_index = len(visual_descripter_file_list)-1
            # print(index_value_init)
            visual_describing_file_name = visual_descripter_file_list[visual_writing_index]
    except:
        visual_writing_index = 0
        # print("last image")
        visual_describing_file_name = visual_descripter_file_list[visual_writing_index]
    display_the_visual_descriptive_writings()
    visual_descriptive_index_level_show_label.configure(
        text=str(str(int(visual_descripter_file_list.index(visual_describing_file_name)) + 1) + " of " + str(
            len(visual_descripter_file_list))))

def right_sub_index_visual_change():
    global _sub_image_index_1, visual_image_file_names, visual_image_index , screenshots_paths , sub_image_visual_descripter_path, visual_descriptive___sub_image____index__show_label
    try:
        if _sub_image_index_1 < (len(visual_image_file_names)):
            _sub_image_index_1 += 1
            sub_image_visual_descripter_path = visual_image_file_names[_sub_image_index_1]
        else:
            _sub_image_index_1 = 0
            sub_image_visual_descripter_path = visual_image_file_names[_sub_image_index_1]
    except:
        _sub_image_index_1 = 0
        sub_image_visual_descripter_path = visual_image_file_names[_sub_image_index_1]
    visual_image_index = screenshots_paths.index(sub_image_visual_descripter_path)
    visual_image_displayer()
    visual_descriptive___sub_image____index__show_label.configure(
        text=str(str(int(visual_image_file_names.index(sub_image_visual_descripter_path)) + 1) + " of " + str(
            len(visual_image_file_names))))



def left_sub_index_visual_change():
    global _sub_image_index_1, visual_image_file_names, visual_image_index , screenshots_paths , sub_image_visual_descripter_path
    try:
        if _sub_image_index_1 > (-1*len(visual_image_file_names)):
            _sub_image_index_1 -= 1
            # print(index_value_init)
            sub_image_visual_descripter_path = visual_image_file_names[_sub_image_index_1]
        else:
            _sub_image_index_1 = len(visual_image_file_names)-1
            # print(index_value_init)
            sub_image_visual_descripter_path = visual_image_file_names[_sub_image_index_1]
    except:
        _sub_image_index_1 = 0
        # print("last image")
        sub_image_visual_descripter_path = visual_image_file_names[_sub_image_index_1]
    visual_image_index = screenshots_paths.index(sub_image_visual_descripter_path)
    visual_image_displayer()
    visual_descriptive___sub_image____index__show_label.configure(
        text=str(str(int(visual_image_file_names.index(sub_image_visual_descripter_path)) + 1) + " of " + str(
            len(visual_image_file_names))))

def show_particular_sub_visual_image():
    global _sub_image_index_1 , visual_image_index, visual_descriptive___sub_image____index__show_label, universal_image_controlling_widget, visual_image_file_names, sub_image_visual_descripter_path
    sub_visual_image_universal_input = int(universal_image_controlling_widget.get())-1
    if sub_visual_image_universal_input <= len(visual_image_file_names)-1:
        if sub_visual_image_universal_input >= 0:
            _sub_image_index_1 = sub_visual_image_universal_input
            # print(index_value_init)
            sub_image_visual_descripter_path = visual_image_file_names[_sub_image_index_1]
            visual_image_index = screenshots_paths.index(sub_image_visual_descripter_path)
            visual_image_displayer()
            visual_descriptive___sub_image____index__show_label.configure(
                text=str(str(int(visual_image_file_names.index(sub_image_visual_descripter_path)) + 1) + " of " + str(
                    len(visual_image_file_names))))


def start_visual_des():
    global ___image_counter___
    ___image_counter___ = 0
    movie_visual_des()

def movie_visual_des():
    global universal_image_controlling_widget, visual_descriptive_writing_window, visual_image_file_names, visual_writing_index,screenshots_paths, ___image_counter___, visual_image_index
    if ___image_counter___ <= len(visual_image_file_names)-1:
        seconds = float(universal_image_controlling_widget.get())
        milli_sec = seconds*1000
        visual_image_index = screenshots_paths.index(visual_image_file_names[___image_counter___])
        visual_image_displayer()
        ___image_counter___+=1
        visual_descriptive_writing_window.after(int(milli_sec), movie_visual_des)

# ================= ------------------------- change these  _sub_image_index_1, visual_image_file_names ------------------------=================
def display_the_visual_descriptive_writings():
    global visual_descripter_file_list, visual_writing_index, content_of_info, title_of_info, screenshots_paths, visual_image_index, visual_describing_file_name, choose_image_index, _sub_image_index_1, visual_image_file_names, visual_descriptive___sub_image____index__show_label
    # visual_describing_file_name = visual_descripter_file_list[int(visual_writing_index)]
    with open("Browser automation software stored encrypted files/Encrypted Visual descriptive writing/"+visual_describing_file_name, "rb") as loading_visual_file:
        dictionary_visual_data = pickle.load(loading_visual_file)
    encrypted_title = dictionary_visual_data["title"]
    encrypted_content = dictionary_visual_data["content"]
    visual_image_file_names = dictionary_visual_data["path"]

    _sub_image_index_1 = 0
    decrypter = Fernet(key_derive())
    decrypted_title = decrypter.decrypt(encrypted_title).decode()
    decrypted_content = decrypter.decrypt(encrypted_content).decode()

    # print(decrypted_title, decrypted_content)
    choose_image_content___ = []
    for i in visual_image_file_names:
        choose_image_content___.append(screenshots_paths.index(i)+1)
        choose_image_content___.append(",")
    index___ = screenshots_paths.index(visual_image_file_names[_sub_image_index_1])
    title_of_info.delete(0, END)
    choose_image_index.delete(0, END)
    content_of_info.delete(0.0, END)
    title_of_info.insert(0, str(decrypted_title))
    content_of_info.insert(END, decrypted_content)
    choose_image_index.insert(0, choose_image_content___[0:-1])
    visual_image_index = index___
    visual_image_displayer()

    visual_descriptive___sub_image____index__show_label.configure(
        text=str("1" + " of " + str(
            len(visual_image_file_names))))
    # refresh__visual_index_label()





def image_choosing():
    global screenshots_paths, choose_image_index, visual_image_paths, visual_image_index
    processing_indices = choose_image_index.get().split(",")
    processed_indices = []
    visual_image_paths = []
    for i in processing_indices:
        processed_indices.append(screenshots_paths[(int(i)-1)])
    for j in processed_indices:
        if j not in visual_image_paths:
            visual_image_paths.append(j)
    visual_image_index = (int(processing_indices[0]))-1
    visual_image_displayer()


def visual_image_displayer():
    global visual_element, decrypted_image, visual_image_index
    decrypt_image_globally(index_value_=int(visual_image_index))
    visual_element.delete()
    original_width_image = decrypted_image.width
    original_height_image = decrypted_image.height
    if original_width_image > 950:
        ratio___ = 950/original_width_image
        decrypted_image = decrypted_image.resize((int(original_width_image*ratio___), int(original_height_image*ratio___)))
    elif original_height_image > 870:
        ratio___ = 870 / original_height_image
        decrypted_image = decrypted_image.resize(
            (int(original_width_image * ratio___), int(original_height_image * ratio___)))

    # if original_width_image < 750:
    #     ratio___ = 750/original_width_image
    #     decrypted_image = decrypted_image.resize((int(original_width_image*ratio___), int(original_height_image*ratio___)))
    # elif original_height_image < 650:
    #     ratio___ = 650 / original_height_image
    #     decrypted_image = decrypted_image.resize(
    #         (int(original_width_image * ratio___), int(original_height_image * ratio___)))

    tk_image = ImageTk.PhotoImage(decrypted_image)
    disl_w = 465
    disl_h = 435
    visual_element.create_image(disl_w, disl_h, anchor="center", image=tk_image)
    visual_element.image = tk_image  # Keeping a reference


def char_scramble(text):
    digested = hashlib.sha1(text.encode()).hexdigest()
    return digested


def save_visual_writing_details_in_a_file():
    global visual_image_paths, content_of_info, title_of_info
    key = key_derive()
    if double_encryption_key_generator(value=key.decode()) == matching_key_hashed:
        image_choosing()
        # curr_time = time.localtime()
        # curr_clock = time.strftime("%H-%M-%S", curr_time)
        time_tag_file_name_format = char_scramble(str(title_of_info.get())) + ".pkl"
        encrypter = Fernet(key)
        encrypted_title = encrypter.encrypt(title_of_info.get().encode())
        encrypted_content = encrypter.encrypt(content_of_info.get(0.0, END).encode())
        pickle_dictionary = {
            "path":visual_image_paths,
            "title":encrypted_title,
            "content":encrypted_content
        }
        # print(pickle_dictionary)
        with open("Browser automation software stored encrypted files/Encrypted Visual descriptive writing/"+time_tag_file_name_format, "wb") as pickle_file_loader:
            pickle.dump(pickle_dictionary, pickle_file_loader)
            print("Successfully created the visual descriptive writing file")
            refresh_visual_descriptive_writing_index_value()
            right_positive____visual___index_change()






def wish_and_say_random_complement_or_quote():
    hour_of_the_day = time.localtime().tm_hour
    if hour_of_the_day < 12:
        wishing_string = "Good-morning Sir, "
    if hour_of_the_day >= 12:
        wishing_string = "Good-evening Sir, "
    List_of_complement_or_quotes = ["You're looking good today!", "You're looking handsome", "you're looking Gorgeous", "Never stop learning something new", "Good to see you... Gentleman!", "Nothing is impossible"]
    random_quote = random.choice(List_of_complement_or_quotes)
    whole_string = wishing_string + random_quote
    return whole_string





def more_info_label(tooltip_Text, abscissa, ordinate, window, Wrap_l, side, side_left_distance_x, side_left_distance_y):
    global tooltip_Text_on_hover
    q_mark = Label(window, text="?", width=2, font=("Arial", 10, "bold"), foreground="white", background="green4", borderwidth=1)
    q_mark.place(x=abscissa, y=ordinate)
    tooltip_Text_on_hover = tooltip_Text
    q_mark.bind("<Enter>", lambda event, tooltip_Text=tooltip_Text_on_hover: tooltip(tooltip_Text, x_p=abscissa, y_p=ordinate, window=window, wrap_l=int(Wrap_l), side=str(side), tool_tip_distance_x_only_left=side_left_distance_x, tool_tip_distance_y_only_left=side_left_distance_y))
    q_mark.bind("<Leave>", lambda event: remove_tooltip())


def tooltip(text_tooltip, x_p, y_p, window, wrap_l, side, tool_tip_distance_x_only_left, tool_tip_distance_y_only_left):
    global solution
    if side == "right":
        proper_x_pos = x_p+(random.randint(50, 60))
        proper_y_pos = y_p+(random.randint(-20, -5))
    elif side == "left":
        proper_x_pos = x_p - tool_tip_distance_x_only_left
        proper_y_pos = y_p - tool_tip_distance_y_only_left
    solution = Label(window, text=text_tooltip, font=("Arial", 10, "italic"), foreground="gray5", background="lightyellow", wraplength=wrap_l, padx=10, pady=10)
    solution.place(x=proper_x_pos, y=proper_y_pos)


def remove_tooltip():
    global solution
    solution.place_forget()

def pop_up_IDLE():
    global programming_area_widget, Output_area_widget
    IDLE_window = Toplevel(Input_Window)
    main_frame_window = Frame(IDLE_window)
    main_frame_window.pack(anchor=CENTER)



    all_button_widget_frame = Frame(main_frame_window)
    all_button_widget_frame.pack(anchor=CENTER, pady=20)
    idle_frame = Frame(main_frame_window)
    idle_frame.pack(anchor=CENTER)
    IDLE_window.title("IDLE")

    save_program_frame___ = Frame(all_button_widget_frame)
    save_program_frame___.grid(row=0, column=0, padx=10)

    name_of_the_program_entry_field = customtkinter.CTkEntry(save_program_frame___, font=("Courier", 15, "bold"),
                                                      corner_radius=50, width=200, placeholder_text="Path/Name")
    name_of_the_program_entry_field.grid(row=0, column=0)
    import_____button = customtkinter.CTkButton(save_program_frame___, text="Import",
                                                font=("Arial", 13, "bold"))
    import_____button.grid(row=0, column=1, padx=5)
    save_program_in_desktop = customtkinter.CTkButton(save_program_frame___, text="Export", font=("Arial", 13, "bold"),)
    save_program_in_desktop.grid(row=0, column=3)

    Run_program = customtkinter.CTkButton(all_button_widget_frame, text="Run",
                                                      font=("Arial", 13, "bold"), fg_color="red2", hover_color="red3", command=run_user_defined_program)
    Run_program.grid(row=0, column=1, padx=30)

    programming_area_widget = customtkinter.CTkTextbox(idle_frame, width=screen_width/2, height=screen_height/2,
                                                   corner_radius=10, border_width=5, font=("Arial", 20), undo=True,
                                                   autoseparators=True, maxundo=20)
    programming_area_widget.grid(row=0, column=0, padx=5, pady=5)

    Quick_recomondation_area_widget = customtkinter.CTkTextbox(idle_frame, width=(screen_width / 4) , height=screen_height / 2,
                                                       corner_radius=10, border_width=5, font=("Arial", 20), undo=True,
                                                       autoseparators=True, maxundo=20)
    Quick_recomondation_area_widget.grid(row=0, column=1, padx=5, pady=5)

    Output_area_widget = customtkinter.CTkTextbox(main_frame_window, width=screen_width , height=screen_height / 4,
                                                       corner_radius=10, border_width=5, font=("Arial", 20), undo=True,
                                                       autoseparators=True, maxundo=20)
    Output_area_widget.pack(anchor=CENTER,  padx=30, pady=5)

    programming_area_widget.insert(END,"|Programming area|")
    Output_area_widget.insert(END, "Output area")

def run_user_defined_program():
    global programming_area_widget, Output_area_widget, USER_VARIABLES, declared_vars_quick_find
    Output_area_widget.delete("0.0", END)
    Output_area_widget.insert(END, "Output\n\n")
    TOKENS = []
    USER_VARIABLES = []
    declared_vars_quick_find = []
    text_ = programming_area_widget.get("0.0", END)
    raw_tokens = tokenize(text=text_, split_char="\n")
    for lines in raw_tokens:
        TOKENS.append(tokenize(text=lines, split_char=" "))
    compiler(tokens=TOKENS)

def tokenize(text, split_char):
    raw_text_form_pr = str(text)
    program_tokens_raw = raw_text_form_pr.split(split_char)
    program_tokens_raw = list(filter(None, program_tokens_raw))
    tokens_processed = []
    full_line_tokens = []
    for exclude_useless in program_tokens_raw:
        token_atr = exclude_useless[0] + exclude_useless[-1]
        if token_atr != "||":
            tokens_processed.append(exclude_useless)
    for exclude_useless_spaces in tokens_processed:
        word = list(exclude_useless_spaces)
        word.insert(0, " ")
        word.extend(" ")
        clear_index_letter_right = 0
        refactored_word = []
        for i in range(len(word)):
            # clears starting spaces
            if word[i] == " ":
                clear_index_letter_right += 1
            else:
                refactored_word = word[clear_index_letter_right:-1]
                break
        clear_index_letter_left = len(refactored_word)
        for i in range(len(refactored_word), 0, -1):
            # clears ending spaces
            if refactored_word[i-1] == " ":
                clear_index_letter_left -= 1
            else:
                refactored_word = refactored_word[0:clear_index_letter_left]
                break
        final_processed_token = ""
        for k in refactored_word:
            final_processed_token += str(k)
        full_line_tokens.append(final_processed_token)
    return full_line_tokens

Maths_operator_list = [
    "+", "-", "*", "/", "^", "//" , "%", "@"
]

def Maths_logic(token):
    global declared_vars_quick_find, USER_VARIABLES
    # checks validity of the math equation
    if token[0] in declared_vars_quick_find:
        z = float(retrieve_variable_data(token[0])[0])
    else:
        z = float(token[0])
    i3 = 0
    for i in range(0, len(token), 2):
        try:
            if token[i+1] in Maths_operator_list:
                i3 += 2
            else:
                print("Error: invalid syntax.")
                break
        except:
            pass
    for i in range(0 ,len(token), 2):
        try:
            if i3 == len(token)-1:
                if token[i+2] in declared_vars_quick_find:
                    r = float(retrieve_variable_data(variable=token[i+2])[0])
                else:
                    r = float(token[i + 2])
                if token[i+1] == "+":
                    z = z + r
                elif token[i+1] == "-":
                    z = z - r
                elif token[i+1] == "*":
                    z = z * r
                elif token[i+1] == "/":
                    z = z / r
                elif token[i+1] == "^":
                    z = z ** r
                elif token[i+1] == "//":
                    z = z // r
                elif token[i+1] == "%":
                    z = z % r
                elif token[i+1] == "@":
                    z = z ** (1/r)
            else:
                print("Error: Invalid syntax")
        except:
            pass
    return z



def show_results_in_console_(text):
    global Output_area_widget
    Output_area_widget.insert(END, text)
    Output_area_widget.insert(END, "\n")


def CONS_keyword(token):

    global USER_VARIABLES, declared_vars_quick_find
    CONS_keys = []
    previous_established_cons_key_index = 2
    if token[1] == "(":
        if token[-1] == ")":
            for i in range(2, len(token)-1, 1):
                current_mini_token = token[i]
                if current_mini_token == ",":
                    CONS_keys.append(token[previous_established_cons_key_index:i])
                    previous_established_cons_key_index = i+1
            CONS_keys.append(token[previous_established_cons_key_index:-1])
            CONS_flatten = []
            for j in range(len(CONS_keys)):
                current__ = CONS_keys[j]
                l = []
                if current__[0] == "ath":
                    for h in range(1, len(current__)):
                        l.append(current__[h])
                    math_result = Maths_logic(token=l)
                    CONS_keys.insert(j, math_result)
                    CONS_keys.remove(current__)
                if current__[0] in declared_vars_quick_find:
                    var_data = retrieve_variable_data(variable=current__[0])
                    CONS_keys.insert(j, var_data)
                    CONS_keys.remove(current__)
            for j in CONS_keys:
                try:
                    for i in j:
                        CONS_flatten.append(i)
                except:
                    CONS_flatten.append(j)
            show_results_in_console_(text=CONS_flatten)




    else:
        show_results_in_console_(text=token[1:])

special_keywords = [
    ">/", "ath", "fc"
]


def variable_declaration(token):
    global USER_VARIABLES, declared_vars_quick_find
    # print(token)
    if token[0] not in special_keywords:
        declared_vars_quick_find.append(token[0])
        USER_VARIABLES.append([token[0], token[2:]])
        # print(USER_VARIABLES, declared_vars_quick_find)

def retrieve_variable_data(variable):
    global USER_VARIABLES
    for i in USER_VARIABLES:
        if i[0] == variable:
            return i[1]




def compiler(tokens):
    global declared_vars_quick_find
    # start_time = time.perf_counter_ns()
    for single_line_token in tokens:
        # print(single_line_token)
        if single_line_token[0].isnumeric() is True:
            # simple mathematics
            result = Maths_logic(token=single_line_token)
            show_results_in_console_(text=result)
        if single_line_token[0] == ">/":
            CONS_keyword(token=single_line_token)
        if single_line_token[1] == "=":
            variable_declaration(token=single_line_token)
        if single_line_token[0] == "fc":
            print(single_line_token)








note_total_data_used_the_following_day(internet_used_in_this_session=0, time_used_in_this_session=0)
heading = wish_and_say_random_complement_or_quote()

customtkinter.set_default_color_theme("green")
# start Input window or the main window
Input_Window = Tk()
# all Windows inside this space
Input_Window.title("Browser Automation Software ( Version - 2 )")  # Configuring the title to the Input window
Input_Window.minsize(width=700, height=290)
Input_Window.maxsize(width=800, height=290)
# --- Main menu ---
main_menu_bar = Menu(Input_Window)  # Configuring a menu
file_menu = Menu(main_menu_bar, tearoff=0)  # creating the File menu
main_menu_bar.add_cascade(label="Settings", menu=file_menu)  # Adding the file menu to main menu
file_menu.add_command(label="Run", command=__run__main___)  # Configuring the run cascade function
file_menu.add_cascade(label="Reset the Entry Fields", command=reset_entry_fields_completely)  # Configuring the reset cascade function
file_menu.add_cascade(label="Change Password", command=pop_up_reset_password_window)
quick_fill_menu = Menu(main_menu_bar, tearoff=0)  # creating the quick menu
main_menu_bar.add_cascade(label="Quick-fill Options", menu=quick_fill_menu)  # Adding the quick menu to main menu
quick_fill_menu.add_command(label="Quick-Fill", command=read_quick_fill)  # Configuring the quick fill cascade function
quick_fill_menu.add_cascade(label="Overwrite Quick-Fill", command=overwrite_quick_fill)  # Configuring the Overwrite Quick Fill cascade function
decrypt_show_menu = Menu(main_menu_bar, tearoff=0)  # creating the Decrypter menu
main_menu_bar.add_cascade(label="Decryption", menu=decrypt_show_menu)  # Adding the Decrypter menu to main menu
decrypt_show_menu.add_cascade(label="Copied Text", command=pop_up_decrypt_and_show_clipboards)  # Configuring the Decrypt Copied text cascade function
decrypt_show_menu.add_cascade(label="Images", command=pop_up_decrypt_encrypted_screenshot_image_window)
decrypt_show_menu.add_cascade(label="Authentication details", command=pop_up_authentication_details_decrypter)  # Configuring the Decrypt Authentication details cascade function
decrypt_show_menu.add_cascade(label="TakeNotes", command=pop_up_takenotes_window)
decrypt_show_menu.add_cascade(label="Visual descriptive writing", command=pop_up_visual_descriptive_writing)


other_options_menu = Menu(main_menu_bar, tearoff=0)  # creating the total_day_Analysis_show_menu
main_menu_bar.add_cascade(label="Others", menu=other_options_menu)  # Adding the total_day_Analysis menu to main menu
other_options_menu.add_cascade(label="Day Analysis", command=pop_up_total_day_analysis)
other_options_menu.add_cascade(label="To-Do list", command=pop_up_TO_DO_window)
other_options_menu.add_cascade(label="Text webscrapper", command=pop_up_text_based_webscrapper)
other_options_menu.add_cascade(label="IDLE", command=pop_up_IDLE)


# --- Main frame ---
Heading = Label(Input_Window, text=heading, font=("Arial", 20), foreground="gray5")
Heading.pack(anchor=CENTER, pady=10)
main_frame = customtkinter.CTkFrame(Input_Window)
main_frame.pack(anchor="center")  # Configured main Frame
# --- Input fields ---
input_field_Frame = LabelFrame(main_frame, padx=10, pady=10, background="white")
input_field_Frame.grid(row=0, column=0)
# --- Input Labels ---
internet_limit_Label = customtkinter.CTkLabel(input_field_Frame, text="Data Limit : ", font=("Arial", 15))
internet_limit_Label.grid(row=0, column=0)  # Internet limit label configured to input_field_Frame
time_limit_Label = customtkinter.CTkLabel(input_field_Frame, text="Time Limit : ", font=("Arial", 15))
time_limit_Label.grid(row=1, column=0)  # Time limit label configured to input_field_Frame
encryption_key_Label = customtkinter.CTkLabel(input_field_Frame, text="Login Password  : ", font=("Arial", 15))
encryption_key_Label.grid(row=2, column=0)
encryption_key_Label = customtkinter.CTkLabel(input_field_Frame, text="Quick-Close : ", font=("Arial", 15))
encryption_key_Label.grid(row=3, column=0)
# --- Input Entries ---
internet_limit_Entry = customtkinter.CTkEntry(input_field_Frame, font=("Arial", 13, "bold"), corner_radius=50, bg_color="white", width=200, placeholder_text="Data limit in Megabytes")
internet_limit_Entry.grid(row=0, column=1)  # Configured the internet limit entry field
time_limit_Entry = customtkinter.CTkEntry(input_field_Frame, font=("Arial", 13, "bold"), corner_radius=50, bg_color="white", width=200, placeholder_text="Time limit in Seconds")  # Configured the time limit entry field
time_limit_Entry.grid(row=1, column=1)  # Configured the time limit entry field
encryption_key_Entry = customtkinter.CTkEntry(input_field_Frame, font=("Arial", 13, "bold"), corner_radius=50, bg_color="white", width=200, show="#", placeholder_text="Password")
encryption_key_Entry.grid(row=2, column=1)
#=======================================================
option_box_var = customtkinter.StringVar(value="Active Window")
option_box = customtkinter.CTkOptionMenu(master=input_field_Frame, values=("Active Window", "Chrome & Edge", "Bluestacks5", "Only Warn", "Minimize"), variable=option_box_var, width=200)
option_box.grid(row=3, column=1, columnspan=1, pady=10, padx=20, sticky="w")
#=========================================================

# --- Get from the Conversion of units, button ---
conversion_get_data_Button = customtkinter.CTkButton(input_field_Frame, text="Convert Gb to Mb", font=("Arial", 13, "bold"), command=convert_data)
conversion_get_data_Button.grid(row=0, column=3)
conversion_get_time_Button = customtkinter.CTkButton(input_field_Frame, text="Convert Min to Sec", font=("Arial", 13, "bold"), command=convert_time)
conversion_get_time_Button.grid(row=1, column=3)
Forgot_password_Button = customtkinter.CTkButton(input_field_Frame, text="Forgot Password", font=("Arial", 13, "bold"), command=pop_up_reset_password_window)
Forgot_password_Button.grid(row=2, column=3)

# --- error Configurations ---
# --- Input Frame configuration ---
Input_Window.config(menu=main_menu_bar)  # Configuring the main menu
# --- the values for internet and time used to show ---
print("Number of cores present in this device - ", processor, "Cores")
if (processor - 3) < 0:
    print("Warning: You Don't have minimum number of Cores in your device ( Minimum cores needed is 3 ), Run the program on your own Risk")
else:
    print("~ This device is eligible to run the program ~")
print("~ Browser Automation Software ( Version - 2 ) Successfully Launched ~")
mainloop()  # Mainloop