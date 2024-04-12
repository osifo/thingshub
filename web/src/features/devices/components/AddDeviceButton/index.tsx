import React, {useState} from "react";
import { Link } from "react-router-dom";
import { useAddDevice } from "../../actions";

const AddDeviceButton = () => {
  const [isLoading, setIsLoading] = useState();

  return (
    <Link to="/new-device">
      <button>Add Device</button>
    </Link>
  )
}

export default AddDeviceButton;