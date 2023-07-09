import grpc
import protos.questions_pb2 as q
import protos.questions_pb2_grpc as q_grpc

def run():
    # open a gRPC channel
    channel = grpc.insecure_channel('localhost:50051')

    # create a stub (client)
    stub = q_grpc.QuestionAnswerStub(channel)

    # create a valid request message
    question = q.QuestionRequest(question="What is pan card")

    # make the call
    response = stub.GetAnswer(question)

    # et voilà
    print(response.answer)

if __name__ == '__main__':
    run()