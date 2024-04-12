import httpUtils from '../../../utils/httpUtils';
import { API_BASE_URL } from '../../../utils/constants'

export const fetchUserDetails = (userId: string) => 
  httpUtils.get({ url: `${API_BASE_URL}/users/userId` });

export const fetchUsers = () => httpUtils.get({
  url: `${API_BASE_URL}/users`
});

export const fetchUserDevices = async (userId: string) => {
  const response = await httpUtils.get({
    url: `${API_BASE_URL}/users/${userId}/devices`
  });

  console.log('response ===== ', response)

  if (response.success) return response.data;
  throw new Error(response.error);
};