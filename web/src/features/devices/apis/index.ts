import httpUtils from '../../../utils/httpUtils';
import { API_BASE_URL } from '../../../utils/constants';

type DeviceT = {
  name: string
  description: string,
  ownerId: string
}

export const addNewDevice = async (device): Promise<DeviceT> => {
  const { ownerId, ...device_params } = device;
  const params = { owner_id: ownerId, ...device_params }
  const response = await httpUtils.post({
    url: `${API_BASE_URL}/devices`,
    requestParams: params
  });

  if (!response.success) {
    throw new Error(JSON.stringify({
      message: response.error,
      status: response.status
    }))
  }

  return response.data
}