import { useQuery, QueryClient, useMutation, InvalidateQueryFilters } from '@tanstack/react-query';
import { addNewDevice }  from '../apis';
import { ServerStateKeys } from '../../../utils/constants'

type DeviceT = {
  name: string
  description: string,
  ownerId: string
}

export const useAddDevice = () => {
  const queryClient = new QueryClient();

  return useMutation({
    mutationFn: addNewDevice,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: [ServerStateKeys.devices] })
    }
  });
}
