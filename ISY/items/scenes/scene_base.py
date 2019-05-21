#! /usr/bin/env python

''' 

Base Scene

Common to all elements returned from rest/nodes/scenes

   properties = list of properties and values

'''



class Scene_Base(object):

    def __init__(self, container, scene_info):
        self.container = container

        self.properties = {'status' : 'ready'} # list of properties key = property name, value = property value

        self.address = scene_info.address
        self.name = scene_info.name
        self.flag = scene_info.flag
        self.container_node_address = scene_info.container_node_address
        self.id = scene_info.id
        self.family = scene_info.family

        self.container_node_address = scene_info.container_node_address
        self.container_type = scene_info.container_type
        self.primary_node = scene_info.primary_node

        self.device_group = scene_info.device_group

        self.controllers = scene_info.controllers
        self.responders = scene_info.responders

    def __str__(self):
        return ("Scene: {} ; address {} ; flag {}; id {}, container {}".format(self.name, self.address, self.flag, self.id, self.container_node_address))

    def process_websocket_event(self,event):
        pass # classes to override

    def add_property(self, property_):
        self.properties [property_] = None

    def set_property(self, property_, value):
        self.properties [property_] = value
        self.container.scene_property_change(self,property_,value) 
 
    def send_request(self,path,query=None,timeout=None): 
        return self.container.send_request(path,query,timeout)

    def device_event(self,device): #device event, process and see if we are interested
        pass # subclasses to provide