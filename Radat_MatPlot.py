""" 
Для відкриття вікна з радаром
"""
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
matplotlib.use('qtAgg')


fig = plt.figure(figsize=(8,4), facecolor="k") #Створюю вікно (задаю параметри)
fig.canvas.manager.set_window_title("Radar") #Встановлюю назву вікна

mgn = plt.get_current_fig_manager() #Запускаю менеджер вікна

ax = fig.add_subplot(1, 1, 1, polar=True, facecolor=(0.1, 0.6, 0.3, 0.2)) #Створюю круглий графік
ax.tick_params(axis="both", colors="w", grid_color=(0.1, 0.6, 0.3, 0.2)) #Ставить галочки
r_max = 200 #Радіус радара
ax.set_ylim([0.0, r_max]) #Межі перегляду осі Y.
ax.set_xlim([0.0, np.pi]) #Межі перегляду осі X.
ax.set_position([-0.5, -0.39, 2, 1.7]) #[зліва, знизу, ширина, висота] або Bbox
ax.set_rticks(np.linspace(0.0, r_max, 15)) #Налаштування поділу сітки на граіфку
ax.set_thetagrids(np.linspace(0.2, 179.8, 19)) #Налаштування ділення сітки на граіфку

line_1, = ax.plot([0,r_max], color='w', linewidth=3.0) #Створюю лінію



ang = 100
line_1.set_data(np.repeat((ang * (np.pi/180)), 2), np.linspace(0.0, r_max, 2))


# plt.show()





######### Тестовий цикл
# Fl = True
# while Fl:
#     line_1.set_data(np.repeat((ang * (np.pi/180)), 2), np.linspace(0.0, r_max, 2))
#     ax.draw_artist(line_1)
#     fig.canvas.blit(ax.bbox)
#     fig.canvas.flush_events()
    
#     print(ang)
#     ang += 0.01
#     if ang >= 180:
#         # ang = 0
#         Fl = False

# plt.close()



# #############################################
"""
Готова анімація з обмеженою кілюкістю даних
"""
# import numpy as np
# import matplotlib
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation
# matplotlib.use('qtAgg')

# fig = plt.figure(figsize=(8,4), facecolor="k") #Створюю вікно (задаю параметри)
# # fig.canvas.toolbar.pack_forget() #Прибираю меню
# fig.canvas.manager.set_window_title("Radar") #Встановлюю назву вікна

# mgn = plt.get_current_fig_manager() #Запускаю менеджер вікна

# ax = fig.add_subplot(1, 1, 1, polar=True, facecolor=(0.1, 0.6, 0.3, 0.2)) #Створюю круглий графік
# ax.tick_params(axis="both", colors="w", grid_color=(0.1, 0.6, 0.3, 0.2)) #Ставить галочки
# r_max = 200 #Радіус радара
# ax.set_ylim([0.0, r_max]) #Межі перегляду осі Y.
# ax.set_xlim([0.0, np.pi]) #Межі перегляду осі X.
# ax.set_position([-0.5, -0.39, 2, 1.7]) #[зліва, знизу, ширина, висота] або Bbox
# ax.set_rticks(np.linspace(0.0, r_max, 15)) #Налаштування поділу сітки на граіфку
# ax.set_thetagrids(np.linspace(0.2, 179.8, 19)) #Налаштування ділення сітки на граіфку

# line_1, = ax.plot([0,r_max], color='w', linewidth=3.0) #Створюю лінію

# # angl = 90 #Кут повороту лінії
# # line_1.set_data(np.repeat((angl * (np.pi/180)), 2), np.linspace(0.0, r_max, 2)) #Додаю параметри до лінії
# # line_1.set_ydata()

# def angle_count(frame, line, radius):
#     line.set_data(np.repeat((frame * (np.pi/180)), 2), radius)
#     return [line]

# rad = np.linspace(0.0, r_max, 2)
# # angle = 1
# angle = np.arange(0, 180, 0.5)
# animation = FuncAnimation(
#     fig=fig,
#     func=angle_count,
#     frames=angle,
#     fargs=(line_1, rad),
#     interval=30,
#     blit=True,
#     repeat=False
# )

# plt.show()
