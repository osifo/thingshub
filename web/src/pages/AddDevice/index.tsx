import React from 'react';
import CreateDeviceForm from '../../features/devices/components/CreateDeviceForm'
import ErrorBoundary  from '../../components/ErrorBoundary'

const AddDevice = () => (
  <ErrorBoundary notification={"Something went wrong while Adding "}>
    <section>
      <div>Add device here</div>
      <CreateDeviceForm />
    </section>
  </ErrorBoundary>
)

export default AddDevice;