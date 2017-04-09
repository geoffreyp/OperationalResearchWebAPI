"""The Python implementation of the GRPC helloworld.Greeter client."""

from __future__ import print_function

import grpc

from protoClassClient import api_pb2_grpc
from protoClassClient import api_pb2


def run():
  channel = grpc.insecure_channel('0.0.0.0:50051')
  stub = api_pb2_grpc.OperationalResearchStub(channel)
  response = stub.InitConversation(api_pb2.InitRequest(customer='Florian', solutionSize=4, evalNb=2, solution='4-3-5'))
  print("Client received: Id" + response.id)
  print("Client received Solution : " + response.solution)


if __name__ == '__main__':
  run()