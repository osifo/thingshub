import { useQuery, useQueryClient, useMutation } from '@tanstack/react-query';
import { fetchUserDevices, addNewDevice }  from '../apis';
import { ServerStateKeys } from '../../../utils/constants'

export const useFetchUserDevices = (userId: string) => {
  return useQuery({
    queryKey: [ServerStateKeys.devices, userId],
    queryFn: () => fetchUserDevices(userId)
  });
}
