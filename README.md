# Visualize PANDA Trajectory prediction dataset

## visualize code step:

1. 读取文件到一个list of json
2. 把数据集按照以下格式组织，为framewise_dataset：
   ``` python
   list [ 
       dict { "frame_id": frame_id, 
           "person_in_frame": OrderedDict{ pid, list [x,y] },
           "scene_id": sceme_id,
   ]
   ```
3. 把数据集按照以下方式组织，为trackwise_dataset：
   ``` python
   dict {
       "scene_info": {"id": 0, "p": 78, "s": 0, "e": 170, "fps": 3}
       "track_info": list [ {"f": 1590, "p": 78, "x": 3.226599931716919, "y": -10.371999740600586},
                            {"f": 1600, "p": 78, "x": 3.2267000675201416, "y": -10.371800422668457}, 
                            ... ]
   }
   ```
**Question**  
应该处理成啥样的dataset？？

