# ****************************************
#
# Learning Micro Python and programming with ESP32
# By: Avi Salmon
# All instructions on https://github.com/avisalmon/single_button
#
# This is a general utility library for the games on the SIngle Button platform 
# ****************************************

import framebuf

class Sprite:
    def __init__(self, x_pos=0, y_pos=0, image=[], size=(8,8), pattern='rect'):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.size = size
        self.image = image
        self.frame = 0
        self.pattern = pattern
        self.animate = False
                
        if self.pattern == 'imag':
            try:
                for index, in_image in enumerate(self.image):
                    with open(in_image, 'rb') as file:
                        image_data = bytearray(file.read())
                    self.image[index] = image_data
                if self.image[0]:
                    self.fbuf = framebuf.FrameBuffer(self.image[0], self.size[0], self.size[1], framebuf.MONO_HLSB)
            except:
                self.fbuf = framebuf.FrameBuffer(bytearray(self.size[0] * self.size[1] * 1), self.size[0], self.size[1], framebuf.MONO_VLSB)
         
        elif self.pattern == 'rect':
            self.fbuf = framebuf.FrameBuffer(bytearray(self.size[0] * self.size[1] * 1), self.size[0], self.size[1], framebuf.MONO_VLSB)
        else:
            self.fbuf = framebuf.FrameBuffer(bytearray(self.size[0] * self.size[1] * 1), self.size[0], self.size[1], framebuf.MONO_VLSB)
            
    def move(self, step_x, step_y):
        self.x_pos += step_x
        self.y_pos +- step_y
        
    def __str__(self):
        return f'<Sprite on x: {self.x_pos} y: {self.y_pos} size: {self.size}>'
    
    def animate_on(self):
        self.animate = True
    
    def animate_off(self):
        self.animate = False
        
    def draw(self, display, offset=0, mask=0):
        display.blit(self.fbuf, self.x_pos, self.y_pos + offset, mask)
        
    def next_frame(self):
        if self.frame == len(self.image)-1:
            self.frame = 0
        else:
            self.frame += 1

        self.fbuf = framebuf.FrameBuffer(self.image[self.frame], self.size[0], self.size[1], framebuf.MONO_HLSB)