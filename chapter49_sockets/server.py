# UDP Version of a Socket Server - note superclasses

import socketserver
import datetime
import traceback

class UDPServerSocketHandler(socketserver.DatagramRequestHandler):

    def handle(self):
        """ method to 'handle' requests - muct be called handle"""
        print('In handle() - method')

        # Receive a message from a client - not different style
        data, client = self.request
        data = data.decode().strip()
        print(f'Received: {data}')
                
        # Generate a repsonse
        timestamp = datetime.datetime \
                            .now() \
                            .strftime('%Y-%m-%d %H:%M:%S')
        result = f'{data} - {timestamp}'
        print(f'Result: {result}')
                
        # Send data back to client
        print('Returning result to client')
        client.sendto(result.encode(), self.client_address)


# To create a UDP server mix in the UDPServer superclass
class MultiThreadedUDPServer(socketserver.ThreadingMixIn, socketserver.UDPServer):
    """ Multi-threaded UDP server"""
    pass


def main():
    print('Starting MultiThreaded UDP Server')

    try:
        server_address = ('127.0.0.1', 8085)

        # Use custom Multithreasded UDP server
        print('Starting up on', server_address)
        server = MultiThreadedUDPServer(server_address, UDPServerSocketHandler)

        print('Activating server')
        server.serve_forever()

    except Exception as exp:
        traceback.print_exc()

if __name__ == '__main__':
    main()
