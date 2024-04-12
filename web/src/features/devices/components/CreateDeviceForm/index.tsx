import React, { useState, useRef, useEffect } from 'react';
import { useAddDevice } from '../../actions';
import {Navigate} from 'react-router-dom';

const CreateDeviceForm = () => {
  const [isCreated, setIsCreated] = useState(false);
  const [userLocation, setUserLocation] = useState();
  const deviceFormRef = useRef();
  const { isError, isSuccess, data: responseData, mutate: addDevice } = useAddDevice();

  useEffect(() => {
    let currentUserLocation: string | null = localStorage.getItem('user_location');
    if (currentUserLocation) {
      setUserLocation(JSON.parse(currentUserLocation));
    } else {
      navigator.geolocation.getCurrentPosition(({coords}) => {
        currentUserLocation = JSON.stringify([coords.latitude.toString(), coords.longitude.toString()]);
        localStorage.setItem('user_location', currentUserLocation)

        setUserLocation(JSON.parse(currentUserLocation));
      })
    }
  }, []);

  const handleAddDevice = (e) => {
    e.preventDefault();
    const formData = new FormData(deviceFormRef.current)
    const device_param = {
      name: formData.get('name')!.toString(),
      description: formData.get('description')!.toString(),
      ownerId: '3',
      last_location: userLocation
    }

    addDevice(device_param, {
      onSuccess: (data, variables, context) => {
        setIsCreated(true) 
      },

      onError: () => console.log("isError ======= ", isError)
    });
  }

  if (isCreated) return <Navigate to="/" />
  return (
    <div>
      <form onSubmit={handleAddDevice} ref={deviceFormRef}>
        <section className="form_section header">
          <div>Create a new device</div>
        </section>

        <section className="form_section body">
            <div>
              <label htmlFor="name">Name</label>
              <input id="name" name="name" type="text" placeholder="Enter a name for this device"/>
            </div>

            <div>
              <label htmlFor="description">Description</label>
              <input id="description" name="description" type="text" placeholder="enter a description"/>
            </div>
        </section>

        <section className="form_section footer">
          <button>Add Device</button>
        </section>
      </form>
    </div>
  )
}

export default CreateDeviceForm;