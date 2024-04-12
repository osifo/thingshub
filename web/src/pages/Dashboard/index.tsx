import React from 'react';
import AddDeviceButton from '../../features/devices/components/AddDeviceButton'
import {useFetchUserDevices} from '../../features/users/actions'

const Dashboard = () => {
  // current_user_id
  const { data: deviceData, isLoading, isError } = useFetchUserDevices('3')
  const renderDevices = () => {
    if(isError) {
      return renderError()
    } 

    if (!deviceData?.length) return renderEmptyNotice(); 

    return (
      <>
        <AddDeviceButton />
        <div>
          { deviceData.map(device => <div key={device.id}>{device.name}</div>) }
        </div>
      </>
    )
  };

  const renderEmptyNotice = () => (
    <div>
      <label>You do not have any devices yet.</label>
      <AddDeviceButton />
    </div>
  );

  const renderLoadingState = () => (
    <div>loading...</div>
  );

  const renderError = () => (<div>Could not load devices</div>);
  
  return (
    <div>
      <label>Dashboard</label>

      <section>
        <header>
          <label>My Devices</label>
          <div>
            {isLoading ? renderLoadingState() : renderDevices()}
          </div>
        </header>
      </section>
      <div>This is the user's dashboard</div>
    </div>
  )
}

export default Dashboard;
