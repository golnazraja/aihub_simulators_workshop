#!/usr/bin/env python
import glob
import os
import sys

try:
    sys.path.append(glob.glob('../carla/dist/carla-0.9.13-py3.8-linux-x86_64.egg'))
except IndexError:
    print(IndexError)

import carla

import random
import time


def main():
    global camera
    actor_list = []

    try:
        
        client = carla.Client('localhost', 2000)
        client.set_timeout(2.0)
        world = client.get_world()
        blueprint_library = world.get_blueprint_library()
        bp = random.choice(blueprint_library.filter('vehicle'))

        if bp.has_attribute('color'):
            color = random.choice(bp.get_attribute('color').recommended_values)
            bp.set_attribute('color', color)

        transform = carla.Transform(carla.Location(x=-43.5, y = 110, z = 0.5), carla.Rotation(yaw=-90))
        vehicle = world.spawn_actor(bp, transform)

        actor_list.append(vehicle)
        print('created %s' % vehicle.type_id)

        #vehicle.set_autopilot(True)

        try:
            vehicle.apply_control(carla.VehicleControl( throttle = 0.5, steer = 0, brake = 0))
        except Exception as e:
            print(e)

        
        camera_bp = blueprint_library.find('sensor.camera.depth')
        camera_transform = carla.Transform(carla.Location(x=1.5, z=2.4))
        camera = world.spawn_actor(camera_bp, camera_transform, attach_to=vehicle)
        actor_list.append(camera)
        print('created %s' % camera.type_id)

        cc = carla.ColorConverter.LogarithmicDepth
        #camera.listen(lambda image: image.save_to_disk('_out/%06d.png' % image.frame, cc))

        # location = vehicle.get_location()
        # location.y -= 40
        # vehicle.set_location(location)
        # print('moved vehicle to %s' % location)

        # #Spawn vehicles in an 80m vicinity of the camera
        # spawn_points = world.get_map().get_spawn_points()
        # vehicle_bp_library = world.get_blueprint_library().filter('vehicle.*')
        # radius = 80
        
        # for spawn_point in spawn_points:
            
        #     vec = [spawn_point.location.x - transform.location.x, spawn_point.location.y - transform.location.y]
        #     if vec[0]*vec[0] + vec[1]*vec[1] < radius*radius:
        #         npc =  world.try_spawn_actor(random.choice(vehicle_bp_library), spawn_point)
        #         if npc is not None:
        #             actor_list.append(npc)
        #             npc.set_autopilot(True)


        time.sleep(5)

    finally:

        print('destroying actors')
        camera.destroy()
        client.apply_batch([carla.command.DestroyActor(x) for x in actor_list])
        print('done.')


if __name__ == '__main__':

    main()
